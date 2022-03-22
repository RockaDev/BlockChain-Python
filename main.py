from hashlib import sha256
import json

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
t1 = blockchain.transaction("Alice","9","Michal")
t2 = blockchain.transaction("Bob","91","Liza")
t3 = blockchain.transaction("Blano","8.1","Fero")
name = str(input("Name: "))
pay = str(input("Amount of BTC: "))
receiver = str(input("Who to send: "))
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

