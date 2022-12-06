import hashlib
import random
import time
 
class Block:
 
    def __init__(self, data: str, previous_hash: bytes) -> None:
        self.data = data
        self.previous_hash = previous_hash
        self.next_block_challenge = random.getrandbits(160) # (2^160 / 2, 2^160)
        self.challenge_result = 0
        self.hash = 0
 
    def __str__(self) -> str:
        return f"{self.data}-{self.previous_hash}-{self.next_block_challenge}-{self.challenge_result}"
 
    def is_valid(self):
        return hashlib.sha1(str(self).encode()) == self.hash
 
    def update_hash(self):
        self.hash = hashlib.sha1(str(self).encode())
 
class BlockChain:
 
    def __init__(self, data) -> None:
        self.chain = [Block(data, 0)]
 
    def get_block(self, i=0):
        return self.chain[i]
 
    def add_new_block(self, data: str):
        last_block = self.chain[-1]
 
        new_block = Block(data, last_block.hash)
        new_block.challenge_result = solve_challenge(last_block.next_block_challenge)
        new_block.update_hash()
 
        self.chain.append(new_block)
 
def solve_challenge(block_hash, challenge):
    # encontrar um x tal que hash(x+block_hash) < challenge
    
    return X
 
begin = time.time()
 
blockchain = BlockChain("genesis")
for _ in range(1000000):
    blockchain.add_new_block("babau")
 
print(time.time() - begin)