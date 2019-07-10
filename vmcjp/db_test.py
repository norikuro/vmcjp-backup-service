#!/usr/bin/env python

import pymongo
import json

from vmcjp.utils import dbutils

class Test(object):
  def db(self):
    db = dbutils.DocmentDb("vmcjp/s3config.json", "sddc_db", "sddc_collection")
    collection = db.get_collection()
#    col = collection.aggregate([{"$project": {"sddc.name": 1}}])
#    collection.remove()
#    col = db.find_with_fields(
#      {}, 
#      {
#        "sddc_updated": 1,
#        "sddc.name": 1, 
#        "sddc.region": 1, 
#        "sddc.num_hosts": 1, 
#        "org.display_name": 1,
#        "customer_vpc.linked_account": 1,
#        "customer_vpc.linked_vpc_subnets_id": 1,
#        "_id": 0
#      }
#    )
#    col = db.find_one({"sddc.name": {"$exists": True}})
#    print(col)
#    col = collection.find()
    col = db.find_with_fields({}, {"_id": 0})
    print(json.dumps(col, indent=4))
#    for data in col:
#      print(json.dumps(data, indent=4))
  
def main():
  test = Test()
  test.db()

if __name__ == '__main__':
  main()
