from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
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


def getmasterimage(email):
    response = table.scan(
        FilterExpression=Attr("email").eq(email)
    )
    print(type(response))
    x=json.dumps(response['Items']) 
    with open("userdata.json", "w") as outfile: 
        outfile.write(x) 
    df = pd.read_json (r'userdata.json')
    df.to_csv(r"userdata.csv",index=None)
    data = pd.read_csv("userdata.csv")
    data.set_index("name", inplace=True)
    #df2 = data.loc['17IT109']
    data.plot.bar()
    saveloc = 'static/maingraph/'+email+'.png'
    plt.savefig(saveloc,bbox_inches='tight')
    return saveloc
