from web3 import Web3, HTTPProvider, IPCProvider
from web3.utils import *
from grove_rgb_lcd import *
from cytoolz.functoolz import curry
import collections
import time
import grovepi


web3 = Web3(HTTPProvider("http://192.168.1.139:8545", request_kwargs={'timeout': 5}))

global currentblock
global numberofshots
global pouring
global button
currentblock = web3.eth.blockNumber
numberofshots = 0
pouring = False
button = 3

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
   	   if mytx['to'] == u'0x5806717dd97a60e47ee2029467e9d8aea10c4849': 
   		print("Ma Fucking Working")
                print(mytx)
                receipt = web3.eth.getTransactionReceipt(tx)
                print(receipt)
		logs = receipt['logs']
                print(logs)
		orderedshots = int(logs[0]['topics'][1], base=16)
                
#                numberofshots += (mytx['value'] / 1000000000000000L)
                numberofshots += orderedshots

def poll_button():
      global pouring
      global numberofshots
      global button

      if pouring == False:
        if grovepi.digitalRead(button) == 1 :
          pouring = True
          numberofshots -= 1

def do_pouring():
       global pouring
       time.sleep(1)
       pouring = False

grovepi.pinMode(button,"INPUT")

while True:
      newblock = web3.eth.blockNumber
      if (currentblock < newblock):
        for block in range(currentblock, newblock):
           new_block_callback(block)
      
#      print("Looping: " + str(web3.eth.blockNumber))
      currentblock = newblock
      poll_button()
      do_pouring()
      setText("Block: {0}\nTokens: {1}".format(currentblock, numberofshots))
      time.sleep(1)
