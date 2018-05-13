import os
import sys
import requests,json

url = "http://127.0.0.1:4103"
payload = '{"jsonrpc":"2.0","method":"getwalletaccounts","params":{"max":9999},"id":123}'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=payload, headers=headers)
jres = json.loads(r.text)
#print(str(jres))
accounts =  jres["result"]
for account in accounts:
    sourceAccount = int(account['account'])
    srcBalance = account["balance"]
    if (srcBalance):
        print("{} with {} pasc".format(sourceAccount,srcBalance))
    print(str(account))
