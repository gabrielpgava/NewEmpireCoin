from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
import pprint
from AccountModel import AccountModel


if __name__ == "__main__":
    
    
    blockchain = Blockchain()
    pool = TransactionPool()

    alice = Wallet()
    bob = Wallet()


    transaction = alice.createTransaction(bob.publicKeyString(),5, 'TRANSFER')

    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)

    coveredTransactions = blockchain.gerCoveredTransactionsSet(pool.transactions)

    print(coveredTransactions)