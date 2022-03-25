import sys
import time
import os
import colorama
import random
from colorama import Fore
from resources import *

#variables
tryAgain = False
subName = False

#counters
failCount = 0
threatCount = 0

#lists
randColor = [Fore.RED, Fore.BLUE]


#FUNCTIONS#
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
def slowload(index):
  clearConsole()
  slowprint2(Fore.GREEN+"""NODE SECURITY ACTIVATED.
INITIALIZING SIGNAL DEBUG PROGRAM""")
  for i in range(index):
    slowprint1(random.choice(randColor)+"\.\     /._.\     /._.\.")
    slowprint1(" \.\   /./ \.\   /./ \.\.")
    slowprint1("  \.\_/./   \.\_/./   \.\.")
    slowprint1("   \.../     \.../     \.")
    time.sleep(0.5)
    clearConsole()
  slowprint1(Fore.GREEN+"TASK FINISHED")
    
  

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