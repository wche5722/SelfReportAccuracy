# import datasheets
# loading estimates
estimateFile = open("finalEditData.csv")
line = estimateFile.readline()
i = 0
estimateData = {}
while line:
    if line[0] == "R":# and line[1] == "_":
        eLine = line.split(",")[3:9]
        cID = eLine[0]
        # only keep Bets placed, outcome of bets (raw and processed)
        tempData = (eLine[1],eLine[2],eLine[5])
        print(tempData)
        # dictionary key is customer ID
        estimateData[cID] = tempData
    line = estimateFile.readline()
    
# load actual customer data
actualFile = open("customerData.csv")
line = actualFile.readline().decode("utf-8-sig").encode("utf-8")

i = 0
actualData = {}
while line and i < 10:
    aLine = line.strip().split(",")
    cID = aLine[0]
    # bets and demographic information
    data = (aLine[1:9])
    # dictionary key is customer Id
    actualData[cID] = data
    line = actualFile.readline()


# get all customerIDs
estimateCustomers = estimateData.keys()
actualCustomers = actualData.keys()

# create headings for new CSV
headers = ['bets', 'estimated outcome', 'cleaned estimate outcome', 'active days', 'bet count', 'bets per active', 'net position', 'race bets', 'sports bets','gender', 'age\n']
head = "customers"
for h in headers:
    head += "," + h
wFile = open("./cleanV1.0.csv", "w")
wFile.write(head)


# if customerID exists in both customer base, combine data into a single line and add to file
for c in estimateCustomers:
    if c in actualCustomers:
        eData = estimateData[c]
        aData = actualData[c]
        jData = "" + c + "," + eData[0]+ "," + eData[1] + "," + eData[2] 
        for a in aData:
            jData += "," + a
        wFile.write(jData + "\n")
    else:
        pass

wFile.close()
