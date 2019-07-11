#!/usr/bin/env python

import json

from vmcjp.utils import sddc_db
from vmcjp.utils import constant
from vmcjp.utils.s3utils import read_json_from_s3

class Config(object):
    def __init__(self):
      f = json.load(open(constant.S3_CONFIG, "r"))
      j = read_json_from_s3(f["bucket"], f["config"])
      self.token = j["token"]
      self.org_id = j["org_id"]
      self.sddc_id = j["sddc_id"]
      self.db = sddc_db.DocmentDb(j["db_url"])
