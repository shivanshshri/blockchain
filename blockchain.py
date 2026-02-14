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


if __name__ == "__main__":
    genesis_block = Block(0, ["Genesis Block"], "0")
    print("Block Hash:", genesis_block.hash)
