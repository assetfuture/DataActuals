# Reading an excel file using Python
import sys
import json
import pandas as pd
import requests
import os
import numpy as np

#py ElermoreGlenActuals.py Maintenance

#API Parameters
KEY = 'd57c8ba4280143b49b4bea1fa07f4baa'
##STAGINGKEY = '522d1a18-9829-4f13-90f0-2370667541d4'
TRANSACTIONALSURL = "https://api.assetfuture.com/plans/Transactionals"
HEADERS = {'Cache-Control': 'no-cache','Ocp-Apim-Subscription-Key': KEY} ##
RECORDCOUNT = 10000
STARTINDEX = 0
PARAMS = {'count': RECORDCOUNT,'startIndex': STARTINDEX}
print (PARAMS)

#CSV File
HEADER_ROW_NUM = 0
INDEX = 1
CSV_FILE =  "Documents\\RFBI_May2025_Actuals2.xlsx"
COL_ASSETID = "AF ID"
COL_MAINTENANCECOST = "Actual costs of maintenance carried out"
COL_MAINTENANCEDATE = "Actual date maintenance carried out"
COL_MAINTENANCETYPE = "Type of maintenance carried out"
COL_REPAIRCOST = "Actual costs of repairs carried out"
COL_REPAIRDATE = "Actual date of repairs carried out"
COL_REPAIRDESCRIPTION = "Description of repairs carried out"
COL_REPLACEMENTDATE = "Actual date replacement carried out" 
COL_REPLACEMENTCOST = "Actual cost of replacement carried out"
ACTIVITYTYPE_MAINTENANCE = "Maintenance"
ACTIVITYTYPE_REPAIRS = "Repairs"
ACTIVITYTYPE_REPLACEMENT = "Replacement"
JSON_FILE = ".\\test.json"
DATA_SHEET = 'Data'
jsonArray = []
try:

    #Read data from excel
    data = pd.read_excel(CSV_FILE, sheet_name=DATA_SHEET, header = 0)

    df = pd.DataFrame(data, columns= [COL_ASSETID,COL_MAINTENANCECOST,COL_MAINTENANCEDATE,
    COL_MAINTENANCETYPE,COL_REPAIRCOST,COL_REPAIRDATE,COL_REPAIRDESCRIPTION,
    COL_REPLACEMENTDATE,COL_REPLACEMENTCOST])

    print(data)


    for index in df.index:
        itemDict = {}
        itemDict["itemReferenceId"] = str(int(df[COL_ASSETID][index]) or '')
        itemDict["referenceId"] = str(int(df[COL_ASSETID][index]) or '')
        #itemDict["referenceId"] = str(int(df["AF ID"][index]) or '')
        if (pd.notnull(df[COL_ASSETID][index])):
            if (pd.notnull(df[COL_REPAIRDATE][index]) 
            and pd.notnull(df[COL_REPAIRCOST][index])):
                itemDict["transactionDate"] = str(df[COL_REPAIRDATE][index])
                itemDict["totalAmount"] = df[COL_REPAIRCOST][index]
                itemDict["transactionType"] = ACTIVITYTYPE_REPAIRS
                itemDict["description"] = str(df[COL_REPAIRDESCRIPTION][index] or '')
                jsonArray.append(itemDict)
            if (pd.notnull(df[COL_REPLACEMENTCOST][index]) 
            and pd.notnull(df[COL_REPLACEMENTDATE][index])):
                itemDict["transactionDate"] = str(df[COL_REPLACEMENTDATE][index])
                itemDict["totalAmount"] = df[COL_REPLACEMENTCOST][index]
                itemDict["transactionType"] = ACTIVITYTYPE_REPLACEMENT
                jsonArray.append(itemDict)
            if (pd.notnull(df[COL_MAINTENANCEDATE][index])
            and pd.notnull(df[COL_MAINTENANCECOST][index])):
                itemDict["transactionDate"] = str(df[COL_MAINTENANCEDATE][index])
                itemDict["totalAmount"] = float(df[COL_MAINTENANCECOST][index])
                itemDict["transactionType"] = ACTIVITYTYPE_MAINTENANCE
                itemDict["transactionSubType"] = str(df[COL_MAINTENANCETYPE][index] or '')
                jsonArray.append(itemDict)

    pd.set_option('display.max_colwidth', None)
    print(df)        

    #Uncomment below code if json data is to be written to file

    jsonString = json.dumps(jsonArray)
    f = open(JSON_FILE, "w")    
    f.write(str(jsonString))
    f.close()

    countRequest = requests.get(url = TRANSACTIONALSURL, json=jsonArray, headers = HEADERS, params = PARAMS)
    count = countRequest.json()
    print('Before Ingestion: ' + str(count["count"]))

    responseItems = requests.post(url = TRANSACTIONALSURL, json=jsonArray, headers = HEADERS)
    response = responseItems.json()
    print(responseItems)

except Exception as e:
    print("Error {0}: {1}".format(e.errno, e.strerror))
    countRequest = requests.get(url = TRANSACTIONALSURL, json=jsonArray, headers = HEADERS, params = PARAMS)
    count = countRequest.json()
    print('After Ingestion: ' + str(count["count"]))