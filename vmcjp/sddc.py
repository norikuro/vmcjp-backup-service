#!/usr/bin/env python

import json
import requests
import atexit

from datetime import datetime
from pytz import timezone
from six.moves.urllib import parse
from vmware.vapi.vmc.client import create_vmc_client
from vmware.vapi.vsphere.client import create_vsphere_client
from com.vmware.vcenter_client import ResourcePool, Folder
from com.vmware.content_client import Library

from vmcjp.config import Config
from vmcjp.utils.metadata import get_members

class SddcConfig(Config):
    def __init__(self):
        super(SddcConfig, self).__init__()
        
        now = datetime.now(timezone("Asia/Tokyo")).strftime("%Y/%m/%d")
        self.db.upsert(
            {"sddc_updated": {"$exists":True}}, 
            {"$set": 
              {"sddc_updated": now}
            }
        )
        
        session = requests.Session()
        self.vmc_client = create_vmc_client(self.token, session=session)
        atexit.register(session.close)

    
    def get_org_config(self):
        sddc_config = {
            "id": self.org_id,
            "display_name": self.vmc_client.Orgs.get(self.org_id).display_name
        }
        
        self.db.upsert(
            {"sddc_updated": {"$exists":True}}, 
            {"$set": 
              {"org": sddc_config}
            }
        )
    
    def get_aws_connected_accounts(self):
        a = []
        accounts = self.vmc_client.orgs.account_link.ConnectedAccounts.get(self.org_id)
        for account in accounts:
            a.append(
                {
                    "account_number": account.account_number,
                    "id": account.id
                }
            )
        sddc_config = {"aws_connected_account": a}

        self.db.upsert(
            {"sddc_updated": {"$exists":True}}, 
            {"$set": 
              {"aws_connected_account": a}
            }
        )
        

    def get_sddc_config(self):
        self.sddc = self.vmc_client.orgs.Sddcs.get(self.org_id, self.sddc_id)
        resource_config = self.sddc.resource_config
        
        sddc_config = {
            "id": self.sddc.id,
            "name": self.sddc.name,
            "num_hosts": len(resource_config.esx_hosts),
            "vpc_cidr": resource_config.vpc_info.vpc_cidr,
            "vmc_version": resource_config.sddc_manifest.vmc_version,
            "region": resource_config.region
        }
        
        self.db.upsert(
            {"sddc_updated": {"$exists":True}}, 
            {"$set": 
              {"sddc": sddc_config}
            }
        )

    def get_vcenter(self):
        vc_url = self.sddc.resource_config.vc_url
        
        self.db.upsert(
            {"sddc_updated": {"$exists":True}}, 
            {"$set": 
              {"vc_url": vc_url}
            }
        )

    def list_user_resourcepools(self):
        management_pools = ["Resources", 
                            "Mgmt-ResourcePool", 
                            "Compute-ResourcePool"]

        self.vsphere = create_vsphere_client(
            parse.urlparse(self.sddc.resource_config.vc_url).hostname, 
            username=self.sddc.resource_config.cloud_username, 
            password=self.sddc.resource_config.cloud_password
        )
        self.vcenter = self.vsphere.vcenter
        rps = self.vcenter.ResourcePool.list(filter=None)
        pools = [rp.name for rp in rps if not rp.name in management_pools]

        self.db.upsert(
            {"sddc_updated": {"$exists":True}}, 
            {"$set": 
              {"resourcepools": pools}
            }
        )

    def list_user_folders(self):
        management_folders = ["Discovered virtual machine", 
                              "VMs migrated to cloud", 
                              "ClonePrepInternalTemplateFolder", 
                              "ClonePrepReplicaVmFolder", 
                              "ClonePrepParentVmFolder", 
                              "ClonePrepResyncVmFolder", 
                              "vm", 
                              "Management VMs", 
                              "Workloads", "Templates"]

        folder_filter_spec = Folder.FilterSpec(type="VIRTUAL_MACHINE")
        fls = self.vcenter.Folder.list(folder_filter_spec)
        folders = [fl.name for fl in fls if not fl.name in management_folders]

        self.db.upsert(
            {"sddc_updated": {"$exists":True}}, 
            {"$set": 
              {"folders": folders}
            }
        )

    def list_contentlibrary(self):
        libs = self.vsphere.content.Library
        lib_ls = libs.list()
        
        a = []
        for id in lib_ls:
          lib = libs.get(id)
          t = str(lib.type)
          if t == "LOCAL":
            a.append({"name": lib.name, "type": t})
          elif t == "SUBSCRIBED":
            a.append({"name": lib.name, 
                      "type": t, 
                      "subscription_url": lib.subscription_info.subscription_url, 
                      "on_demand": lib.subscription_info.on_demand,
                      "automatic_sync_enabled": lib.subscription_info.automatic_sync_enabled})
            
        self.db.upsert(
            {"sddc_updated": {"$exists":True}}, 
            {"$set": 
              {"contentlibraries": a}
            }
        )

def lambda_handler(event, context):
    sddc_operations = SddcConfig()
    sddc_operations.get_org_config()
    sddc_operations.get_aws_connected_accounts()
    sddc_operations.get_sddc_config()
    sddc_operations.get_vcenter()
    sddc_operations.list_user_resourcepools()
    sddc_operations.list_user_folders()
    sddc_operations.list_contentlibrary()

def main():
    sddc_operations = SddcConfig()
    sddc_operations.get_org_config()
    sddc_operations.get_aws_connected_accounts()
    sddc_operations.get_sddc_config()
    sddc_operations.get_vcenter()
    sddc_operations.list_user_resourcepools()
    sddc_operations.list_user_folders()
    sddc_operations.list_contentlibrary()

if __name__ == '__main__':
    main()
