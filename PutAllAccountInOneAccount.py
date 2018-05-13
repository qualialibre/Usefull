import os
import sys
import requests,json

print("usage: account source_max_balance max_account_counts_to_process")
targetAccount = int(sys.argv[1])
sourceAccountMaxBalance = int(sys.argv[2])
maxCount = int(sys.argv[3])

url = "http://127.0.0.1:4103"
payload = '{"jsonrpc":"2.0","method":"getwalletaccounts","params":{"max":99999},"id":123}'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=payload, headers=headers)

i = 0
jres = json.loads(r.text)
accounts =  jres["result"];
for account in accounts:
    sourceAccount = int(account['account'])
    if sourceAccount != targetAccount:
        srcBalance = account["balance"] - 0.0001
        if (srcBalance > 0.0001) and (srcBalance < sourceAccountMaxBalance):
            for coin in range(0, int(srcBalance)):
                transferPayload = '{"jsonrpc":"2.0","method":"sendto","params":{"sender":' + str(sourceAccount) + ',"target":'+str(targetAccount)+',"amount":' + str(coin)+ ',"fee":0.0001,"payload":"BEEFBABE","payload_method":"aes","pwd":"donthackme"},"id":123}'
                r = requests.post(url, data=transferPayload, headers=headers)
                jres = json.loads(r.text)
                #print(str(jres))
                if 'result' in jres:
                    print(jres['result']['optxt'])
                else:
                    print("Error. account " +str(sourceAccount) + " Error : " + str(jres['error']))    
            i = i  +1
            if (i > maxCount):
                break
                