#TASKS (11p)
#To use the requests library you have to install it first. If you have pip and you're using python3 interpreter in your project
# then simply pip3 install requests

# 1 Find another public API with cryptocurrency and compare prices. As an output print:
# "Currently the XXX exchange market is better for buying whilst YYY is better for selling" (3p)
# 2 Use https://randomuser.me API to download a random user data.
# Create and store 100 random users with ids, username, name (first + last name) using this API (2p)
# 3 Prepare a simulation of transactions between these users
# Take random user and pair him/her with another one. Assume a random amount but take real world price. Sum up the transaction printing:
# username1 exchanged X.XXX BTC with username2 for PLN YYYYY.YYY PLN. (2p)
# Simulate real time - do not proceed all transactions at once. Try to make around 100 transactions per minute (2p)
# Simulate user's assets. Creating a user assign random amount of a given currency. Take it into account while performing a transaction.
# Remember to amend user's assets after the transaction. (2p)

import requests
import random
from time import sleep
# 1 task
def bitbay():
    response_bitbay = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
    data_bitbay = response_bitbay.json()
    best_bid_bitbay=data_bitbay['bid']
    best_ask_bitbay=data_bitbay['ask']
    return best_bid_bitbay, best_ask_bitbay
best_bid_bitbay, best_ask_bitbay = bitbay()
print('Bitbay:\nbid:',best_bid_bitbay,'ask:',best_ask_bitbay)

response_bitmarket = requests.get("https://www.bitmarket.pl/json/BTCPLN/ticker.json")
data_bitmarket = response_bitmarket.json()
best_bid_bitmarket=data_bitmarket['bid']
best_ask_bitmarket=data_bitmarket['ask']
print('\n Bitmarket: \nbid:',best_bid_bitmarket,'ask:',best_ask_bitmarket)
print("Currently the %s exchange market is better for buying whilst %s is better for selling" %
      ("Bitbay" if best_bid_bitmarket < best_bid_bitbay else "Bitmarket", "Bitbay" if best_ask_bitmarket > best_ask_bitbay else "Bitmarket"))

# 2 task
Data = []
while len(Data) != 100:
    try:
        data = requests.get("https://randomuser.me/api/?results=10&inc=login,name").json()
        for i in data['results']:
            Data.append(i)
    except:
        pass

Users = {}
for i in range(100):
    Users[i] = {'username': Data[i]['login']['username'], 'name' : {'first': Data[i]['name']['first'], 'second' : Data[i]['name']['last']},
                'pocket': {"BTC" : round(random.random()*2,8), "PLN": round(random.random()*30000,2)}}


for i in range(100):
    #sleep(0.5)
    transaction = [random.randint(0, 99), random.randint(0, 99)]
    bid, ask = bitbay()
    User1 = Users[transaction[0]]['pocket']
    User2 = Users[transaction[1]]['pocket']
    btc = round(random.random(),8)
    pln = round(btc * bid,2)
    while btc > User1['BTC'] or pln > User2['PLN']:
        btc = round(random.random(),8)
        pln = round(btc * bid,2)
    print("\nTransaction %s\n%s to %s sold %s BTC for %s PLN" %(i, Users[transaction[0]]['username'], Users[transaction[1]]['username'], btc, pln))
    # Users[transaction[0]]['pocket']['BTC'] -= btc
    # Users[transaction[1]]['pocket']['BTC'] += btc
    # Users[transaction[0]]['pocket']['PLN'] += pln
    # Users[transaction[1]]['pocket']['PLN'] -= pln

for i in range(100):
    print("Username: %s\n BTC: %s\n PLN: %s" %(Users[i]['username'],Users[i]['pocket']['BTC'], Users[i]['pocket']['PLN']))


