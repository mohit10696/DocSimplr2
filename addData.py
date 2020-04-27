
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
def upload():
	dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
	table = dynamodb.Table('resumedata')
	with open("resumedata.json") as json_file:
	    movies = json.load(json_file, parse_float = decimal.Decimal)
	    for movies in movies:
	        table.put_item(Item=movies)
        

