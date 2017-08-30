from web3 import Web3, HTTPProvider, IPCProvider
from web3.utils import *
from grove_rgb_lcd import *
from cytoolz.functoolz import curry
import collections
import time


web3 = Web3(HTTPProvider("http://192.168.1.139:8545", request_kwargs={'timeout': 5}))

global currentblock
global numberofshots
currentblock = web3.eth.blockNumber
numberofshots = 0

def new_block_callback(block_number):
       global numberofshots
       print("New Block: {0}".format(block_number))
       block = web3.eth.getBlock(block_number)
       #print(len(block.transactions))

       for tx in block.transactions:
         mytx = web3.eth.getTransaction(tx)
         print(type(mytx))
#         if str(type(mytx)) is not "cytoolz.functoolz.curry":
         if not isinstance(mytx, curry):
           print(mytx['to'])
   	   if mytx['to'] != u'0x7ffdf119323243f43991cbe80687f7f1c5791129': 
   		print("Ma Fucking Working")
                print(mytx)
                receipt = web3.eth.getTransactionReceipt(tx)
                print(receipt)
                numberofshots += (mytx['value'] / 1000000000000000L)

while True:
      newblock = web3.eth.blockNumber
      if (currentblock < newblock):
        for block in range(currentblock, newblock):
           new_block_callback(block)
      
#      print("Looping: " + str(web3.eth.blockNumber))
      currentblock = newblock
      setText("Block: {0}\nTokens: {1}".format(currentblock, numberofshots))
      time.sleep(1)
