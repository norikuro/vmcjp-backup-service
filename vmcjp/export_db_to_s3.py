import json
#import pymongo

from vmcjp.utils import sddc_db
from vmcjp.utils import constant
from vmcjp.utils.s3utils import read_json_from_s3

class ExportDBtoS3(object):
  def __init__(self):
    f = json.load(open(constant.S3_CONFIG, "r"))
    j = read_json_from_s3(f["bucket"], f["config"])
    self.buket = f["bucket"]
    self.db = sddc_db.DocmentDb(j["db_url"])    
  
  def export(self):
    cur = self.db.find_with_fields(
      {}, 
      {"_id": 0}
    )
#    json.dumps(cur, indent=4)
    write_json_to_s3(self.bucket, "sddc.json", cur)
  
def lambda_handler(event, context):
  export_operations = ExportDBtoS3()
  export_operations.export()

def main():
  export_operations = ExportDBtoS3()
  export_operations.export()

if __name__ == '__main__':
  main()
