import csv
import json

NATURE_PAYABLE = "PAYABLE"
NATURE_RECEIVABLE = "RECEIVABLE"

entitySymbols = {
    "Tata Steel Limited": "TSL",
    "Tata BlueScope Steel Ltd": "TATA BLUESCOPE"
}


def process_row(row): 
    row["type"] = NATURE_PAYABLE if row["type"] == "Payable" else NATURE_RECEIVABLE if row["type"] == "Receivable" else row["type"]
    entity1, entity2 = row["reconEntity"].split("-")
    _entity1, _entity2 = row["reconSet"].split("-")
    entity1, entity2, _entity1, _entity2 = entity1.strip(), entity2.strip(), _entity1.strip(), _entity2.strip()
    if entity1 == _entity1 and entity2 == _entity2:
        row["entity1"] = entity1
        row["entity2"] = entity2
    elif entity1 == _entity2 and entity2 == _entity1:
        row["entity1"] = entity2
        row["entity2"] = entity1
    else:
        print(entity1, entity2, _entity1, _entity2)
        raise "Invalid Entity Set Relation"
    
    row["nature"] = row["type"]
    row["code"] = row["vendorCustomerCode"]
    del row["reconEntity"]
    del row["reconSet"]
    del row["type"]
    del row["vendorCustomerCode"]
    row["symbol"]=entitySymbols[row["companyName"]]
    return row


with open("./inputs/VendorCustomer.csv") as csvfile:
    csvReader = csv.DictReader(csvfile)
    jsonFileName = "./outputs/vendorCustomer.jsonl"
    jsonfile = open(jsonFileName,'w')
    for row in csvReader:
        if row["companyName"] == "Tata BlueScope Steel Pvt":
            continue
        row = process_row(row)
        json.dump(row, jsonfile)
        jsonfile.write("\n")
