from BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
import pprint



if __name__ == "__main__":
    
    sender="sender"
    receiver="receiver"
    amount=1
    type="TRANSFER"
    
    wallet = Wallet()
    fraudulentWallet = Wallet()
    blockchain = Blockchain()
    pool = TransactionPool()


    transaction = wallet.createTransaction(receiver,amount,type)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)
    
    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 1
    block = wallet.createBlock(pool.transactions, lastHash, blockCount)

    if not blockchain.lastBlockHashValid(block):
        print ('lastBlockHash is not valid')

    if not blockchain.blockCountValid(block):
        print ('blockCount is not valid')


    if blockchain.lastBlockHashValid(block) and blockchain.blockCountValid(block):
        blockchain.addBlock(block)


    pprint.pprint(blockchain.toJson())


    