import os
import sys
import requests,json

class Infos:
    def __init__(self):
        self.pubkey = ""
        self.balance = 0
        self.accounts = []
        

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
        srcBalance = float(acnt["balance"])
        if (srcBalance > 0.001):
            sourceAccount = int(acnt['account'])
            name = acnt["name"]
            pubkey = acnt["enc_pubkey"]
            element = [x for x in accounts if x.pubkey == pubkey]
            if (len(element)):
                element[0].balance = element[0].balance + srcBalance
                element[0].pubkey = pubkey
                element[0].accounts.append((sourceAccount,name))
            else:
                element = Infos()
                element.balance = srcBalance
                element.pubkey = pubkey
                element.accounts.append((sourceAccount,name))
                accounts.append(element)

except:
       pass
       
print("found {} accounts".format(len(accounts)))
accounts.sort(key=lambda x: x.balance)

for a in accounts:
    if a.balance > minBalance:
        acclist = []
        acclistN = []
        acc = ""
        if (len(a.accounts) > 1):
            for an in a.accounts:
                acclist.append(an[0])
                acclistN.append(an[1])
                if (len(an[1]) > 0):
                    acc += str(an) + ", "
        if len(acc) == 0:
            acc = str(a.accounts[0])
        
        f.write("pubkey: {} balance: {} accounts_count: {} accounts: {} names: {}\n".format(a.pubkey, round(a.balance,2), len(a.accounts), str(acclist), str(acclistN)))
        print("Balance {0: <13} accounts+name {1: <1} count {2: <1}".format(round(a.balance,2), acc, len(a.accounts)))
   
f.close()
print("results saved in AccountList.txt")