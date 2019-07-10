# vmc-demo

## Abstract
SDDC.py will back up VMware Cloud on AWS configurations like following information to AWS DocumentDB and S3.
* VMware Cloud on AWS SDDC's id and name.
* Number of hosts
* Management CIDR block
* SDDC version
* Resource Pools, Folders, Content Libraries

network.py will back up VMware Cloud on AWS's network configurations like following information to AWS DocumentDB and S3.
* Connected customer AWS VPC
* Security Groups (user created groups)
* Firewall Rules (user created fws)
* Segments (user created routed and extended segments)
* VPN (L3VPN and L2VPN) configuration

You can run this script on AWS EC2 or AWS Lambda.

## Scrips
followings are main scripts
* vmcjptool/sddc.py
* vmcjptool/networks.py

followings are helper scripts
* vmcjptool/*.py
* vmcjptool/network/*.py
* vmcjptool/utils/*.py

## How to...
### Configure AWS Endpoint and deploy EC2 instance
First you need to configure AWS Endpoint to be able to access S3 from EC2.
Deploy EC2 instance.
Configure awscli on EC2 instance with following command.
execute "aws s3 ls" command and check if the command was list your S3 buckes successfully.
```cmd
# aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: (your region id, like us-west-2)
Default output format [None]: (Enter)

# aws s3 ls
```

### Clone vmc-demo to local

```cmd
# git clone https://github.com/norikuro/vmc-demo.git
```

### Set PYTHONPATH to be able to import librarys  
```cmd
# export PYTHONPATH=${PWD}:$PYTHONPATH
```

### Prepare config files
We need following JSON files to run this script.  

| file          | file localtion | description |
|---|---|---|
| s3config.json | vmc-demo | This file contains S3 information like bucket and file name. |
| config.json | S3 | This file contains VMC's org id, SDDC's id, refresh token. |

#### config file example
* s3config.json
  * location: vmc-demo/s3config.json
```cmd
{
  "bucket": "vmc-env", #S3 bucket name
  "config": "config.json" #config file name 
}
```

* config.json
  * location: s3://vmc-env/config.json  
vmc-env is bucket name, specified in s3config.json
```cmd
{
  "org_id": "VMC's Organization ID",
  "sddc_id": "SDDC ID",
  "token": "Refresh token number",
  "db_url": "mongodb://<user name for DocumentDB>:<password for DocumentDB>@docdb-xxxxxxxxxx.cluster-xxxxxx.ap-northeast-1.docdb.amazonaws.com:27017/",
}
```

### Run scripts
* run sddc.py or network.py
** After run these scripts successfully, scrips will create/update sddc.json or network.json on S3's same bucket.
** You can see backed up VMC's configuration data in sddc.json or network.json
```cmd
$ python sddc.py
```
