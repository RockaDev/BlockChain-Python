from hashlib import sha256
import json
import random,sys

class BlockChain(object):
    def __init__(self):
        self.value = 0
        self.chain = []
        self.pending_transactions = []
        self.transactions = []

    def transaction(self,name,amount,receiver):
        hashed = sha256(amount.encode()).hexdigest()
        trans = {
            "name":name,
            "amount":hashed,
            "receiver":receiver
        }
        self.transactions.append(trans)


blockchain=BlockChain()
t1 = blockchain.transaction("Alice",f"{random.randint(1,100)}","Michal")
t2 = blockchain.transaction("Bob",f"{random.randint(1,100)}","Liza")
t3 = blockchain.transaction("Blano",f"{random.randint(1,100)}","Fero")
name = str(input("Name: "))
pay = str(input("Amount of BTC: "))
if pay.isdigit():
    receiver = str(input("Who to send: "))
else:
    print("Amount must contain only numbers!")
    sys.exit()
t4 = blockchain.transaction(name,pay,receiver)

#SAVE FILE
with open(file="clients.txt",mode="a") as clients:
    clients.truncate(0)
    for transaction in blockchain.transactions:
        clients.write(json.dumps(transaction))
    clients.close()

#PRINT TRANSACTIONS
for transaction in blockchain.transactions:
    print(transaction)
