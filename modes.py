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


def start():
  resources.clearConsole()
  characters.InitializeCharDicts()
  ifs.nameBlock1()
  ifs.op1()