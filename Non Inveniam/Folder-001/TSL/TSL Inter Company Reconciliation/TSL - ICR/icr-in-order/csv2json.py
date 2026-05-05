import csv 
import json
import sys

filename = sys.argv[1]

csvfile = open(filename,'r')

jsonFileName = filename.replace(".csv","_json.json")
jsonfile = open(jsonFileName,'w')

fielsnames = ("companyCode", "companyName", "sapDocNo", "reference", "sapDocType", "businessArea", "branchOralloc", "fiscalYear", "postingPeriod", "docChqDate", "postingDate", "amountinLocalCurrency", "localCurrency", "amountinDocumentCurrency", "documentCurrency", "discountBaseAmount", "gstAmount", "netAmount", "withholdingTaxBaseAmount", "withHoldingTaxAmount", "vendorCustomer", "vendorCustomerName", "tradingPartner", "text", "hdrText", "invSOReference", "Plant", "purchasingDocument", "deliveryNote", "account", "accountDescription", "offsettingAccount", "offsettingAcctName", "grirOffsettingAccount", "finalOffsettingAccount", "finalOffsettingAcctName", "wbsElement", "postingKey", "debitCredit", "specialGLInd", "reversalIndicator", "clearingDocNo", "clearingDate", "entrydate", "entryTime" "notionalGST", "grossAmountInLocalCurrency", "deIndicator", "poLine", "entryLine")
# fielsnames = ("blicrEntitynm",
# "blicrGlcode",
# "blicrGlname",
# "blicrBshypacc",
# "blicrBshypaccname",
# "blicrBshypcus2",
# "blicrBsform2",
# "blicrBsexclude",
# "blicrPlhypacc",
# "blicrPlhypname",
# "blicrPlhypcustom2",
# "blicrPlform2",
# "blicrPlexclude",
# "blicrBsexcludeHyp",
# "blicrPlexcludeHyp")
reader = csv.DictReader(csvfile,fielsnames)
for row in reader:
    json.dump(row,jsonfile)
    jsonfile.write('\n')





# {"companyCode", "companyName", "sapDocNo", "reference", "sapDocType", "businessArea", "branchOralloc", "fiscalYear", "postingPeriod", "docChqDate", "postingDate", "amountinLocalCurrency", "localCurrency", "amountinDocumentCurrency", "documentCurrency", "discountBaseAmount", "gstAmount", "netAmount", "withholdingTaxBaseAmount", "withHoldingTaxAmount", "vendorCustomer", "vendorCustomerName", "tradingPartner", "text", "hdrText", "invSOReference", "Plant", "purchasingDocument", "deliveryNote", "account", "accountDescription", "offsettingAccount", "offsettingAcctName", "grirOffsettingAccount", "finalOffsettingAccount", "finalOffsettingAcctName", "wbsElement", "postingKey", "debitCredit", "specialGLInd", "reversalIndicator", "clearingDocNo", "clearingDate", "entrydate", "entryTime" "notionalGST", "grossAmountInLocalCurrency", "deIndicator", "poLine", "entryLine"}
# {"sapOwner", "tableType", "companyCode", "companyName", "sapDocNo", "reference", "sapDocType", "businessArea", "branchOralloc", "fiscalYear", "postingPeriod", "docChqDate", "postingDate", "amountinLocalCurrency", "localCurrency", "amountinDocumentCurrency", "documentCurrency", "discountBaseAmount", "gstAmount", "netAmount", "withholdingTaxBaseAmount", "withHoldingTaxAmount", "vendorCustomer", "vendorCustomerName", "tradingPartner", "text", "hdrText", "invSOReference", "Plant", "purchasingDocument", "deliveryNote", "account", "accountDescription", "offsettingAccount", "offsettingAcctName", "grirOffsettingAccount", "finalOffsettingAccount", "finalOffsettingAcctName", "wbsElement", "postingKey", "debitCredit", "specialGLInd", "reversalIndicator", "clearingDocNo", "clearingDate", "entrydate", "entryTime" "notionalGST", "grossAmountInLocalCurrency", "deIndicator", "poLine", "entryLine"}


# ("blicrEntitynm",
# "blicrGlcode",
# "blicrGlname",
# "blicrBshypacc",
# "blicrBshypaccname",
# "blicrBshypcus2",
# "blicrBsform2",
# "blicrBsexclude",
# "blicrPlhypacc",
# "blicrPlhypname",
# "blicrPlhypcustom2",
# "blicrPlform2",
# "blicrPlexclude",
# "blicrBsexcludeHyp",
# "blicrPlexcludeHyp")