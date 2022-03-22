import sys
import time
import os
import colorama
from colorama import Fore
from resources import *


def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):
    command = 'cls'
    os.system(command)

#indents
def indent():
  print(" ")

def indentPoint5x2():
  time.sleep(0.5)
  print(" ")
  time.sleep(0.5)

#loading animations
def slowload():
  slowprint2(Fore.GREEN+"""NODE SECURITY ACTIVATED.
INITIALIZING SIGNAL DEBUG PROGRAM""")
  for i in range(3):
    slowprint3(""". . .""")
  

#SLOWPRINTS#
#change the divisor to mess with timing
#higher the number the faster it goes
    
def slowprint1(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./50)

def slowprint2(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./25) 

def slowprint3(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./5) 