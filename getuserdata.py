from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import csv
import os
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

cemail = "null"
cresponse = "null"
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
    if(os.stat("userdata.json").st_size == 2):
        return 'static/maingraph/nodata.png'
    df = pd.read_json (r'userdata.json')
    df.to_csv(r"userdata.csv",index=None)
    data = pd.read_csv("userdata.csv")
    data.set_index("name", inplace=True)
    #df2 = data.loc['17IT109']
    data.plot.bar()
    saveloc = 'static/maingraph/'+email+'.png'
    plt.savefig(saveloc,bbox_inches='tight')
    return saveloc

def resumename(email):
    global cemail
    global cresponse
    if(email == cemail):
        response = cresponse
    else:
        response = table.scan(
            FilterExpression=Attr("email").eq(email)
        )
        cresponse = response
        cemail = email
    output = []
#print(table.__dict__)
#print(response)
    response = response['Items']
#print(response)
    for i in response:
        output.append(i['name'])
    return output

def getoneuserdata(name,email):
    response = table.scan(
        FilterExpression=Attr("email").eq(email) & Attr("name").eq(name)
    )
    output = {}
    response = response['Items']
    for i in response:
        for j in i:
            if(j == 'email' or j == 'name'):
                continue
            output[j] = float(i[j]) 
    return output

def resumesum(email):
    global cemail
    global cresponse
    if(email == cemail):
        response = cresponse
        print("working")
    else:
        response = table.scan(
            FilterExpression=Attr("email").eq(email)
        )
        cresponse = response
        cemail = email
    output = []
#print(table.__dict__)
#print(response)
    response = response['Items']
#print(response)
    
    for i in response:
        sum = 0
        for j in i:
            if(j=="name" or j =="email"):
                continue
            #print(i[j])
            sum = sum + float(i[j])
        output.append(sum)
    return output

def topskill(email):
    global cemail
    global cresponse
    if(email == cemail):
        response = cresponse
    else:
        response = table.scan(
            FilterExpression=Attr("email").eq(email)
        )
        cresponse = response
        cemail = email
    output = []
    response = response['Items']
    skill = "notfound"
    for i in response:
        max = 0
        for j in i:
            #print(j)
            #break
            if(j=="name" or j =="email"):
                continue
            #print(i[j])
            if(float(i[j]) > max):
                #print(str(i[j])+skill)
                max = float(i[j])
                skill = j
                continue
            if(float(i[j]) == max):
                #print(str(i[j])+skill)
                max = float(i[j])
                skill = skill +","+ j
        output.append(skill)
    return output

def toplanguage(email):
    global cemail
    global cresponse
    if(email == cemail):
        response = cresponse
    else:
        response = table.scan(
            FilterExpression=Attr("email").eq(email)
        )
        cresponse = response
        cemail = email
    output = []
    response = response['Items']
    skill = "notfound"
    lng = ["Java","C/C++","Python","PHP","Python",".Net"]
    for i in response:
        max = 0
        for j in i:
            #print(j)
            #break
            if(j=="name" or j =="email" or j not in lng):
                continue
            #print(i[j])
            if(float(i[j]) > max):
                #print(str(i[j])+skill)
                max = float(i[j])
                skill = j
                continue
            if(float(i[j]) == max):
                #print(str(i[j])+skill)
                max = float(i[j])
                skill = skill +","+ j

        output.append(skill)
    return output

