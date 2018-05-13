import os
import sys
import requests,json

print("usage: source_account max_coins_to_send dest_account1, dest_account2,...")
sourceAccount = int(sys.argv[1])
maxCoinsToSend = int(sys.argv[2])
targetAccounts = []
for i in range(3, len(sys.argv)):
    targetAccounts.append( int(sys.argv[i]) )

url = "http://127.0.0.1:4103"
payload = '{"jsonrpc":"2.0","method":"getaccount","params":{"account":' + sys.argv[1] + '},"id":123}'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=payload, headers=headers)

i = 0
jres = json.loads(r.text)
account =  jres["result"];
srcBalance = account["balance"] - 0.0001
if (srcBalance > 0.0001):
    for coin in range(0, maxCoinsToSend):
        for targetAccount in targetAccounts:
            transferPayload = '{"jsonrpc":"2.0","method":"sendto","params":{"sender":' + str(sourceAccount) + ',"target":'+str(targetAccount)+',"amount":' + str(1.001)+ ',"fee":0.0001,"payload":"BEEFBABE","payload_method":"aes","pwd":"donthackme"},"id":123}'
            r = requests.post(url, data=transferPayload, headers=headers)
            jres = json.loads(r.text)
            #print(str(jres))
            if 'result' in jres:
                print(jres['result']['optxt'])
            else:
                print("Error. account " +str(sourceAccount) + " Error : " + str(jres['error']))    
            coin = coin + 1
            