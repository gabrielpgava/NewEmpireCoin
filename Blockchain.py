from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel


class Blockchain():

    def __init__(self):
        self.blocks = [Block.genesis()]
        self.accountModel = AccountModel()


    def addBlock(self,block):
        self.blocks.append(block)


    def toJson(self):
        data = {}
        jsonBlocks = []


        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        
        data['blocks'] = jsonBlocks	
        
        return data


    def blockCountValid(self,block):
        if self.blocks[-1].blockCount == block.blockCount - 1:
            return True
        else:
            return False


    def lastBlockHashValid(self, block):
        latestBlockchainHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()

        if latestBlockchainHash == block.lastHash:
            return True
        else:
            return False


    def gerCoveredTransactionsSet(self,transactions):
        covertedTransactions = []
        for transaction in transactions:
            if self.transactionCovered(transaction):
                covertedTransactions.append(transaction)
            else:
                print('Transaction not covered')
        return covertedTransactions


    def transactionCovered(self,transaction):
        senderBalancer = self.accountModel.getBalance(transaction.senderPublicKey)

        if senderBalancer >= transaction.amount:
            return True
        else:
            return False