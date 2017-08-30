from web3 import Web3, HTTPProvider, IPCProvider
from web3.utils import *
from cytoolz.functoolz import curry
import collections
import time


web3 = Web3(HTTPProvider("http://192.168.1.139:8545", request_kwargs={'timeout': 5}))

global currentblock
currentblock = web3.eth.blockNumber

def new_block_callback(block_number):
       print("New Block: {0}".format(block_number))
       block = web3.eth.getBlock(block_number)
       #print(len(block.transactions))

       for tx in block.transactions:
         mytx = web3.eth.getTransaction(tx)
         print(type(mytx))
#         if str(type(mytx)) is not "cytoolz.functoolz.curry":
         if not isinstance(mytx, curry):
           print(mytx['to'])
   	   if mytx['to'] == u'0x63c1d076e990f34b288a4fba56606e0185f4f641': 
   		print("Ma Fucking Working")
                print(mytx)

while True:
      newblock = web3.eth.blockNumber
      if (currentblock < newblock):
        for block in range(currentblock, newblock):
           new_block_callback(block)
      
#      print("Looping: " + str(web3.eth.blockNumber))
      currentblock = newblock
      time.sleep(1)
