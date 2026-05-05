
import csv
import json

tsl_payable = []
tbsl_receivable = []
entitySymbols = {
    "Tata Steel Limited": "TSL",
    "Tata BlueScope Steel Ltd": "TATA BLUESCOPE",
    # "Tata BlueScope Steel Pvt": "TATA BLUESCOPE"
}

ORG_ID = "1632768818522574484"

def process_lineitem(row):
    row["orgId"] = ORG_ID
    row["symbol"] = entitySymbols[row["companyName"]]
    if row["discountBaseAmount"] == None:
        row["discountBaseAmount"] = "0"
    return row


with open("./inputs/TSL-TBSL TSL Payable.csv") as csvfile:
    csvReader = csv.DictReader(csvfile)
    jsonFileName = "./outputs/tsl-tbsl tsl-payable.jsonl"
    jsonfile = open(jsonFileName,'w')
    for row in csvReader:
        row = process_lineitem(row)
        json.dump(row, jsonfile)
        jsonfile.write("\n")
    
with open("./inputs/TSL-TBSL TBSL Receivable.csv") as csvfile:
    csvReader = csv.DictReader(csvfile)
    jsonFileName = "./outputs/tsl-tbsl tbsl-receivable.jsonl"
    jsonfile = open(jsonFileName,'w')
    for row in csvReader:
        row = process_lineitem(row)
        json.dump(row, jsonfile)
        jsonfile.write("\n")

