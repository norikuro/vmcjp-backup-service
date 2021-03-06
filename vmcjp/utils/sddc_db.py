import json
import pymongo

from vmcjp.utils.s3utils import read_json_from_s3
from vmcjp.utils import constant

class DocmentDb(object):
  def __init__(self, url):
    self.client = pymongo.MongoClient(url)
    self.db = self.client[constant.SDDC_DB]
    self.collection = self.db[constant.SDDC_COLLECTION]
    
  def get_client(self):
    return self.client
  
  def get_db(self):
    return self.db
  
  def get_collection(self):
    return self.collection
  
  def upsert(self, query, update_data):
    self.collection.update(query, update_data, upsert=True)

  def find_with_fields(self, query, fields):
    return self.collection.find(query, fields)[0]
  
  def find(self, query):
    cur = self.collection.find(query)
    if cur.count() != 0:
      return cur[0]
    else:
      return

  def remove(self, data_to_remove):
    self.collection.remove(data_to_remove)
