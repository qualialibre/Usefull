import os
import sys
import requests,json

#ListBiggestAccounts 10000
minBalance = int(sys.argv[1])

url = "http://127.0.0.1:4103"
payload = '{"jsonrpc":"2.0","method":"getwalletaccounts","params":{"max":99999},"id":123}'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=payload, headers=headers)
jres = json.loads(r.text)
#print(str(jres))
accounts =  jres["result"]
bigAccounts = []
for account in accounts:
    sourceAccount = int(account['account'])
    srcBalance = account["balance"]
    if (srcBalance > minBalance):
        bigAccounts.append((srcBalance, sourceAccount))

bigAccounts.sort()
for a in bigAccounts:
    print("Account {0: <7} balance {1: <5}".format(a[1], a[0]))