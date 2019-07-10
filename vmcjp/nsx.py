#!/usr/bin/env python

import time
import requests
import atexit

from datetime import datetime
from pytz import timezone
from com.vmware.nsx_policy_client_for_vmc import create_nsx_policy_client_for_vmc
from com.vmware.nsx_vmc_app_client_for_vmc import create_nsx_vmc_app_client_for_vmc

from vmcjp.config import Config
from vmcjp.utils.metadata import get_members
from vmcjp.network.security_groups import get_security_groups
from vmcjp.network.firewall_rules import get_firewall_rules
from vmcjp.network.vpns import get_l3vpns

class NetworkConfig(Config):
    def __init__(self):
        super(NetworkConfig, self).__init__()
        
        now = datetime.now(timezone("Asia/Tokyo")).strftime("%Y/%m/%d")
        self.db.upsert(
            {"sddc_updated": {"$exists":True}}, 
            {"$set": 
              {"network_updated": now}
            }
        )
        
        start = time.time()
        session = requests.Session()
        self.nsx_policy_client = create_nsx_policy_client_for_vmc(
            refresh_token=self.token,
            org_id=self.org_id,
            sddc_id=self.sddc_id,
            session=session
        )
        self.nsx_app_client = create_nsx_vmc_app_client_for_vmc(
            refresh_token=self.token,
            org_id=self.org_id,
            sddc_id=self.sddc_id,
            session=session
        )
        atexit.register(session.close)
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    def list_customer_vpcs(self):
        start = time.time()
        vpc = self.nsx_app_client.infra.LinkedVpcs.list().results[0]
        network_config = {
            "linked_vpc_address": vpc.linked_vpc_addresses[0],
            "linked_account": vpc.linked_account,
            "linked_vpc_subnets_cidr": vpc.linked_vpc_subnets[0].cidr,
            "linked_vpc_subnets_id": vpc.linked_vpc_subnets[0].id,
            "linked_vpc_subnets_availability_zone": vpc.linked_vpc_subnets[0].availability_zone,
            "linked_vpc_id": vpc.linked_vpc_id,
            "route_table_id": vpc.route_table_ids[0]
        }
        self.db.upsert(
            {"network_updated": {"$exists":True}},
            {"$set": 
              {"customer_vpc": network_config}
            }
        )
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
        
    def list_security_groups(self):
        start = time.time()
        network_config = [
            get_security_groups("mgw", self.nsx_policy_client),
            get_security_groups("cgw", self.nsx_policy_client)
        ]
        self.db.upsert(
            {"network_updated": {"$exists":True}},
            {"$set": 
              {"security_groups": network_config}
            }
        )
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    def list_firewall_rules(self):
        start = time.time()
        network_config = [
            get_firewall_rules("mgw", self.nsx_policy_client),
            get_firewall_rules("cgw", self.nsx_policy_client)
        ]
        self.db.upsert(
            {"network_updated": {"$exists":True}},
            {"$set": 
              {"firewall_rules": network_config}
            }
        )
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    
    def list_segments(self):
        start = time.time()
        segments = self.nsx_policy_client.infra.tier_1s.Segments.list("cgw").results
        test = [
            {
                "create_user": segment.get_field("create_user"),
                "display_name": segment.get_field("display_name"),
                "domain_name": segment.get_field("domain_name"),
                "l2_extension": segment.get_field("l2_extension"),
                "subnet": segment.get_field("subnets")[0].to_dict(),
                "type": segment.get_field("type")
            }
            for segment in segments 
            if segment.get_field("create_user") != "admin"
        ]
        print(test)
        network_config = [
            {
                "create_user": segment.get_field("create_user"),
                "display_name": segment.get_field("display_name"),
                "type": segment.get_field("type")
            }
            for segment in segments 
            if segment.get_field("create_user") != "admin"
        ]
        self.db.upsert(
            {"network_updated": {"$exists":True}},
            {"$set": 
              {"segments": network_config}
            }
        )
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    def list_l3vpns(self):
        start = time.time()
        network_config = get_l3vpns(self.nsx_policy_client)
        self.db.upsert(
            {"network_updated": {"$exists":True}},
            {"$set": 
              {"l3vpn": network_config}
            }
        )
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

def lambda_handler(event, context):
    network_operations = NetworkConfig()
    network_operations.list_customer_vpcs()
    network_operations.list_security_groups()
    network_operations.list_firewall_rules()
    network_operations.list_segments()
    network_operations.list_l3vpns()

def main():
    network_operations = NetworkConfig()
    network_operations.list_customer_vpcs()
    network_operations.list_security_groups()
    network_operations.list_firewall_rules()
    network_operations.list_segments()
    network_operations.list_l3vpns()

if __name__ == '__main__':
    main()
