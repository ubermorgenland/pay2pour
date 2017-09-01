from web3 import Web3, HTTPProvider, IPCProvider
from web3.utils import *
from grove_rgb_lcd import *
from cytoolz.functoolz import curry
import collections
import time
import grovepi
from subprocess import call
import requests 

for _ in range(10):
    try:
	web3 = Web3(HTTPProvider("http://173.212.249.235:2000"))
        break
    except requests.exceptions.ReadTimeout:
	print "ReadTimeout"
	time.sleep(1)
        pass
    except requests.exceptions.ConnectionError:
	print "ConnectionError"
	time.sleep(1)
	pass

global currentblock
global numberofshots
global pouring
global button
global relay

currentblock = 0
for _ in range(10):
  try:
    currentblock = web3.eth.blockNumber
    break
  except requests.exceptions.ReadTimeout:
    print "ReadTimeout"
    time.sleep(1)
    pass
  except requests.exceptions.ConnectionError:
    print "ConnectionError"
    time.sleep(1)
    pass
numberofshots = 5
pouring = False
button = 8
relay = 7

grovepi.pinMode(button,"INPUT")
grovepi.pinMode(relay,"OUTPUT")

def new_block_callback(block_number):
       global numberofshots
       print("New Block: {0}".format(block_number))
       block = web3.eth.getBlock(block_number)

       for tx in block.transactions:
         mytx = web3.eth.getTransaction(tx)
         print(type(mytx))
         if not isinstance(mytx, curry):
           print(mytx['to'])
   	   if mytx['to'] == u'0xefb4844e94238b4fa96967cea9cb069b082fbbb7': 
   		print("Ma Fucking Working")
                print(mytx)
                receipt = web3.eth.getTransactionReceipt(tx)
                print(receipt)
		logs = receipt['logs']
                print(logs)
		orderedshots = int(logs[0]['topics'][1], base=16)
                
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
           time.sleep(12)
	   print("sleep done")
           grovepi.digitalWrite(relay, 0)
           pouring = False
	   print("aus")
	 else:
           print "No shots available"
       elif grovepi.digitalRead(button) == -1:
 	   call(["avrdude", "-c", "gpio", "-p", "m328p"])
	   time.sleep(.5)

while True:
      newblock = 0
      for _ in range(10):
        try:
          newblock = web3.eth.blockNumber
          break
        except requests.exceptions.ReadTimeout:
          print "ReadTimeout"
          time.sleep(1)
          pass
        except requests.exceptions.ConnectionError:
          print "ConnectionError"
          time.sleep(1)
          pass
      if (currentblock < newblock):
        for block in range(currentblock, newblock):
           new_block_callback(block)
      
      currentblock = newblock
      do_pouring()
      setText("Block: {0}\nTokens: {1}".format(currentblock, numberofshots))
      time.sleep(1)
