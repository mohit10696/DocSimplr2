#!/usr/bin/python
import csv , json
def convert(email):
	csvFilePath = "sample.csv"
	jsonFilePath = "resumedata.json"
	arr = []
	#read the csv and add the arr to a arrayn

	with open (csvFilePath) as csvFile:
	    csvReader = csv.DictReader(csvFile)
	    for csvRow in csvReader:
	        csvRow['email']=email
        	arr.append(csvRow)
	#print(arr)
	with open(jsonFilePath, "w") as jsonFile:
	    jsonFile.write(json.dumps(arr, indent = 4))
