import csv
import json

NATURE_PAYABLE = "PAYABLE"
NATURE_RECEIVABLE = "RECEIVABLE"

ORG_ID = "1632768818522574484"

entitySymbols = {
    "Tata Steel Limited": "TSL",
    "Tata BlueScope Steel Ltd": "TATA BLUESCOPE"
}


def process_row(row):
    row["orgId"] = ORG_ID
    row["symbol"] = entitySymbols[row["Entity_Name"]]
    row["nature"] = NATURE_PAYABLE if row["nature"] == "Payable" else NATURE_RECEIVABLE if row["nature"] == "Receivable" else row["nature"]
    row["toReport"] = (row["toReport"] == "Yes")
    return row


with open("./inputs/Accounts.csv") as csvfile:
    csvReader = csv.DictReader(csvfile)
    jsonFileName = "./outputs/accounts.jsonl"
    jsonfile = open(jsonFileName,'w')
    for row in csvReader:
        if row["Entity_Name"] == "Tata BlueScope Steel Pvt":
            continue
        row = process_row(row)
        json.dump(row, jsonfile)
        jsonfile.write("\n")
