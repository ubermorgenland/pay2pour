from web3 import Web3, HTTPProvider, IPCProvider
from web3.utils import *
from grove_rgb_lcd import *
from cytoolz.functoolz import curry
import collections
import time
import grovepi


web3 = Web3(HTTPProvider("http://192.168.1.112:8545", request_kwargs={'timeout': 5}))

global currentblock
global numberofshots
global pouring
global button
global relay

currentblock = web3.eth.blockNumber
numberofshots = 0
pouring = False
button = 2
relay = 3

grovepi.pinMode(button,"INPUT")
grovepi.pinMode(relay,"OUTPUT")

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


def do_pouring():
       global pouring
       global relay
       global numberofshots
       global button
       print numberofshots
       print grovepi.digitalRead(button)
       if grovepi.digitalRead(button) == 1:
	 print grovepi.digitalRead(button)
         if numberofshots >= 1:
           print("Starting pour")
           numberofshots -= 1
	   print("decremented")
           grovepi.digitalWrite(relay, 1)
	   print("an")
	   print("sleep")
           time.sleep(10)
	   print("sleep done")
           grovepi.digitalWrite(relay, 0)
           pouring = False
	   print("aus")
         else:
           print "No shots available"

while True:
      newblock = web3.eth.blockNumber
      if (currentblock < newblock):
        for block in range(currentblock, newblock):
           new_block_callback(block)
      
#      print("Looping: " + str(web3.eth.blockNumber))
      currentblock = newblock
      do_pouring()
      setText("Block: {0}\nTokens: {1}".format(currentblock, numberofshots))
      time.sleep(1)
