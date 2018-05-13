import os
import sys
import requests,json

#return a float from a stirng including null/empty string
def ToFloat(str):
    fval = 0.0;
    try:
        fval = float(str.strip())
    except:
        pass
    return fval

print("usage: sourceAccount targetAccount {amount}")
sourceAccount = int(sys.argv[1])
targetAccount = int(sys.argv[2])
trxAmount = 0.0
if (len(sys.argv) > 3):
    trxAmount = ToFloat(sys.argv[3])


headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
url = "http://127.0.0.1:4103"
getBalancePayload = '{"jsonrpc":"2.0","method":"getaccount","params":{"account":' + str(sourceAccount) + '}},"id":123}'
r = requests.post(url, data=getBalancePayload, headers=headers)
jres = json.loads(r.text)
result = jres["result"]
if (trxAmount + 0.0001) > 0.0001:
    srcBalance = trxAmount
else:
    srcBalance = (result["balance"]) - 0.0001

if (srcBalance > 0.0001):
    transferPayload = '{"jsonrpc":"2.0","method":"sendto","params":{"sender":' + str(sourceAccount) + ',"target":'+str(targetAccount)+',"amount":' + str(srcBalance)+ ',"fee":0.0001,"payload":"BEEFBABE","payload_method":"aes","pwd":"donthackme"},"id":123}'
    r = requests.post(url, data=transferPayload, headers=headers)
    jres = json.loads(r.text)
    #print(str(jres))
    if 'result' in jres:
        print(jres['result']['optxt'])
    else:
        print("Error. account " +str(sourceAccount) + " Error : " + str(jres['error']))
else:
	print("Nothing to transfer")
