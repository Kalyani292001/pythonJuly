class Bank:
    def __init__(self,fn,accno,bal):
        self.fullName = fn
        self.account = accno
        self.balance = bal
        self.transactions = []
        # deposit()
    def deposit(self,amount):
            self.balance = self.balance + amount
            self.transactions.append(amount)
            return self.balance
    # withdrawl()
    def withdrawl(self,amount):
        if(self.balance > amount):
            self.balance = self.balance - amount
            self.transactions.append(amount)
        else:
            print("in sufficient balance")

    # last5transactions
    def lastFiveTransactions(self):
        return self.transactions[-5:]


amol = Bank("amol hadole",43,10000)
dhanvi = Bank("dhanvi bangal",56,4000)
kalyani = Bank("kalyani hadole",21,7000000)
pradnya = Bank("pradnya kadam",43,7000)
aryan = Bank("aryan pawar",54,2000)


accs = [amol,dhanvi,kalyani,pradnya,aryan]
for acc in accs:
    print(acc.balance)
for acc in accs:
    print(acc.fullName)
for acc in accs:
    print(acc.transactions)

# deposit()

for acc in accs:
    acc.deposit(100000)
    acc.deposit(100)
    acc.deposit(10)
    acc.deposit(100)

for acc in accs:
    print(acc.balance)

for acc in accs:
    print(acc.fullName ,acc.lastFiveTransactions())