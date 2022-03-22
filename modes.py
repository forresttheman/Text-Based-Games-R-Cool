import sys
import colorama
from colorama import Fore
import time
import random
import os
import modes
import resources
from resources import *
from modes import *
import characters
from characters import *
import ifs
from ifs import *


#lists
atts = ["a cool", "a lovely", "an epic", "a fabulous", "a nice", "a good"]
nameTitles = []

def start():
  resources.clearConsole()
  ifs.nameBlock1()


def op1():
  ifs.op1()