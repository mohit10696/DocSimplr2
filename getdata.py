from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import pandas as pd
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('resumedata')


response = table.scan(
        FilterExpression=Attr("email").eq("abc@gmail.com")
    )

#print(table.__dict__)
print(type(response))
x=json.dumps(response['Items']) 

with open("userdata.json", "w") as outfile: 
    outfile.write(x) 
df = pd.read_json (r'userdata.json')
df.to_csv(r"userdata.csv",index=None)
