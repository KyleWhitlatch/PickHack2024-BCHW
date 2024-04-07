from solcx import compile_standard, install_solc
from web3 import Web3, HTTPProvider, utils
import json

class sc_deployer:
    def __init__(self):
        self.BLOCKCHAIN_IP = '127.0.0.1'
        self.BLOCKCHAIN_PORT = '7545'
        self.w3 = Web3(HTTPProvider("http://{}:{}".format(self.BLOCKCHAIN_IP, self.BLOCKCHAIN_PORT)))
        print("BC CONNECTED: " + str(self.w3.is_connected()))
        self.eth_acct = self.w3.eth.accounts[0]
        install_solc("0.8.0")
        
        with open('..\\eth_src\\contracts\\transact.sol', 'r') as file:
            cont = file.read()
            self.artifact_contract = compile_standard(
                {
                    "language": "Solidity",
                    "sources": {"transact.sol": {"content": cont}},
                    "settings": {
                        "outputSelection": {
                            "*": {"*": ["abi", "metadata", "evm.bytecode"]}
                         }
                    },
                },
                solc_version="0.8.0"
            )
        #print(self.artifact_contract['contracts']['transact.sol']['transact']['abi'])
        self.cont_bytecode = self.artifact_contract['contracts']['transact.sol']['transact']['evm']['bytecode']['object']
        #print(self.cont_bytecode)
        self.cont_abi = self.artifact_contract['contracts']['transact.sol']['transact']['abi']
    def deploy(self, str_to_hash):
        cont = self.w3.eth.contract(abi=self.cont_abi, bytecode= self.cont_bytecode)
        tx_hash = cont.constructor(Web3.to_bytes(hexstr=str_to_hash)).transact({'from': self.eth_acct})
        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        print("Contract Address: {}, type of address {}: ".format(tx_receipt.contractAddress, type(tx_receipt.contractAddress)))
        print("Stored Hash: " + str(self.w3.eth.contract(address=Web3.to_checksum_address(tx_receipt.contractAddress), abi=self.cont_abi).functions.gethash().call()))
        return str(tx_receipt.contractAddress)
    
    def call_checker(self, addr, hash):
        cont = self.w3.eth.contract(address=Web3.to_checksum_address(addr.lower()), abi=self.cont_abi)
        stored_hash = cont.functions.gethash().call()
        print("STORED HASH" + str(stored_hash))
        return cont.functions.compareHash(Web3.to_bytes(hexstr=hash)).call()
    

# test = sc_deployer()
# test.deploy('32768BFEBFBFF000B06713234087911424002538BA01504BD5100020227328012345')
# print(test.call_checker('0xCb0155352c9ACFc02Ee70f57820bD82b7D222A41', '0xea6a63765d8d80f92dd19d559f6e3a862b3e10733a6ebb089069a39d8df0994e'))
        