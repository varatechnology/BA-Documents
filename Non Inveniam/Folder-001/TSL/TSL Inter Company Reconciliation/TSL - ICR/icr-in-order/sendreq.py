import requests
import json
# from TBSL_rec_vals import values
# from TSL_pay_vals import values
from TSL_grir_vals import values as grir_entry
# from TSL_total import values
# from TSL_provision_vals import values
# from coaVals import values
# from time import sleep
from pay_ordered import values as main_entry
from pay_Unordered import values as wild_entry
import sys, getopt

entryType = ''

def main():
    argv = sys.argv[1:] 
    global entryType
    global numPos
    try:
        opts, args = getopt.getopt(argv, "s:t:")
    except getopt.GetoptError:
        sys.exit(2)
    for option, value in opts:
        if option == "-s" and value != '':
            numPos = int(value)
        if option == "-t":
            if value in ["main", "grir", "wild"]:
                entryType = value
            else:
                print("Not a valid type: [main, grir, wild]")
                exit(2)
    
    print(opts, args)





lineItems = {
    "main": main_entry,
    "wild": wild_entry,
    "grir": grir_entry,
}

numPos = 0

URL = 'http://172.25.15.43:9000/sapdataentry'
# # URL = 'http://172.25.15.43:9000/sapGRIRdataentry'

# URL = 'http://localhost:9000/sapdataentry'
# # URL = 'http://localhost:9000/sapGRIRdataentry'
# # URL = 'http://localhost:9000/insertLookupcoaRow'




if __name__ == "__main__":
    main()
    if not entryType in ["main", "grir", "wild"]:
        print("Not a valid type: [main, grir, wild]")
        print("pass argument with -t flag")
        exit(2)
    if entryType == "grir":
        URL = 'http://172.25.15.43:9000/sapGRIRdataentry'
    values = lineItems[entryType]
    preview = {"sapDocNo": values[numPos]["sapDocNo"], "reference": values[numPos]["reference"]}
    yes = input(f"First document is \n {preview}\n\nDo you want to continue? (y/n)")
    if yes == "yes" or yes == "y":
        nLineItems = len(values)
        iterator = range(numPos, nLineItems)
        print(f"Sending data of type == {entryType}")
        for i in iterator:
        # PARAMS = {values}
            r = requests.post(url=URL,json=values[i])
            numPos += 1
            progress = int(100*numPos/nLineItems)
            outputStr = f"Completed {numPos}/${nLineItems}[" + "="*(progress//5) + " "*(20-progress//5) + f"] {progress}%"
            print(outputStr)
        # sleep(0.1)

# print("Successfully call api : ",numPos, end="\r")
