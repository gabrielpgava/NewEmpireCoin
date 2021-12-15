


class TransactionPool:

    def __init__(self):
        self.transactions = []


    def addTransaction(self, transaction):
        self.transactions.append(transaction)


    def transactionExists(self, transaction):
        for poolTransaction in self.transactions:
            if transaction.equals(poolTransaction):
                return True
        return False