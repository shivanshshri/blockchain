import hashlib
import time
import json


class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }

        block_string = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print("Block mined!")
        print("Hash:", self.hash)


class Blockchain:
    def __init__(self):
        self.difficulty = 4
        self.chain = [self.create_genesis_block()]
        

    def create_genesis_block(self):
        genesis_block = Block(0, ["Genesis Block"], "0")
        genesis_block.mine_block(self.difficulty)
        return genesis_block

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        previous_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            transactions=transactions,
            previous_hash=previous_block.hash
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

        return True




if __name__ == "__main__":
    my_blockchain = Blockchain()

    my_blockchain.add_block(["Alice -> Bob : 5 BTC"])
    my_blockchain.add_block(["Bob -> Charlie : 2 BTC"])

    print("Is blockchain valid?", my_blockchain.is_chain_valid())


