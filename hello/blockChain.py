# {
#      "index":0, #索引
#     "timestamp":"",#时间戳
#     "transactions":[#交易信息
#         {
#             "sender":"",#发送者
#             "recipient":"",#接受者
#             "acount":"",#账户
# 
#         }
#     ],
#     "proof":"",#证明
#     "previous_hash":"",#前一个的哈希
# }

import hashlib
import json
from time import time, sleep
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse
from uuid import uuid4


class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # 创世纪区块
        self.new_block(proof=100, previous_hash=1)

    # 新添加一个块

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        # 交易已经打包成区块了,当前的交易就没有了,交易清空交易信息
        self.current_transactions = []
        self.chain.append(block)
        return block

    # 添加一个新的交易
    def new_transaction(self, sender, recipient, amount) -> int:
        """
        :param sender: Address of the Sender发送者
        :param recipient: Address of the recipient接收者
        :param amount: Amount交易的金额
        :return: the Index of the block that will hold this transaction
        """
        # 将交易信息封装到交易信息里
        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount,
            }
        )

        return self.last_block['index'] + 1

    # 标注为静态方法
    # 计算hash值

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    # 获取当前区块链的最后一个区块
    @property
    def last_block(self):
        return self.chain[-1]

    # 工作量证明,不停地验证
    def proof_of_work(self, last_proof: int) -> int:
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        print(proof)
        return proof
    # 验证是否是以4个0开始的
    def valid_proof(self, last_proof: int, proof: int) -> bool:
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        sleep(1)
        # if guess_hash[0:4] == "0000":
        #     return True
        # else:
        #     return False
        print(guess_hash)
        return guess_hash[0:4] == "0000"


#  创建一个实例
testPow = BlockChain()
testPow.proof_of_work(100)
