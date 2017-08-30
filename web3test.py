from web3 import Web3, HTTPProvider, IPCProvider
import time
from grove_rgb_lcd import *
from grovepi import *


web3 = Web3(HTTPProvider("http://192.168.1.139:8545", request_kwargs={'timeout': 5}))

global currentblock
currentblock = 0

def new_transaction_callback(block_hash):
    global currentblock
    print(web3.eth.blockNumber)

    if web3.eth.blockNumber > currentblock:
       currentblock = web3.eth.blockNumber


       print("New Block: {0}".format(block_hash))
       block = web3.eth.getBlock(block_hash['blockHash'])
       setText(str(web3.eth.blockNumber))
       #print(len(block.transactions))

       for tx in block.transactions:
         #print(tx)
         mytx = web3.eth.getTransaction(tx)
         if mytx is not None:	
   	   if mytx['to'] == u'0x63c1d076e990f34b288a4fba56606e0185f4f641': 
   		print("Ma Fucking Working")
                print(mytx)

#new_transaction_filter = web3.eth.filter({ "toBlock": "latest" })
new_transaction_filter = web3.eth.filter('latest')
new_transaction_filter.watch(new_transaction_callback)

while new_transaction_filter.running:
      time.sleep(1)
