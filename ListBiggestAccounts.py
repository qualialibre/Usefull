import os
import sys
import requests,json

#NOTE: normal wallet default port is 4003, Testnet is 4103
if len(sys.argv) != 3:
	print("usage : ListBiggestAccounts.py LocalWalletPort MinimumBalance\nNOTE: normal wallet default port is 4003, Testnet is 4103")
	exit()

port = int(sys.argv[1])
minBalance = int(sys.argv[2])

f = open("AccountList.txt", "w")

url = "http://127.0.0.1:{}".format(port)
print("connecting to {}".format(url))
accounts = []
try:
    #for a in range(0, 999):
    for a in range(0, 2000000):
        if (a%500) == 0:
            print("scanning account {} to {}".format(a, a+500))
        payload = '{"jsonrpc":"2.0","method":"getaccount","params":{"account":' + str(a) + '},"id":123}'
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, data=payload, headers=headers)
        jres = json.loads(r.text)
        #print(str(jres))
        acnt =  jres["result"]
        sourceAccount = int(acnt['account'])
        srcBalance = acnt["balance"]
        if (srcBalance > minBalance):
            name = acnt["name"]
            accounts.append((srcBalance, sourceAccount, name))
except:
       pass
       
print("found {} accounts".format(len(accounts)))
accounts.sort()
for a in accounts:
    msg = "Account {0: <7} balance {1: <20} name '{2: <1}'".format(a[1], a[0], a[2])
    f.write(msg + "\n")
    print(msg)
   
f.close()
print("results saved in AccountList.txt")