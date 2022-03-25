import time
import modes
import resources
from resources import *
from modes import *
import characters
from characters import *

#player stats/variables
morality = 100 #0 is completely murderous, uncaring, 200 is angelic and wonderful, 100 is neutral
antagonize = 0 
#adds up, if passes threshold, character gets mad at you. Have diff aggression levels for repeated bad/good actions

#char lists
characterList = []
char1MoralitySaved = []


#antagonize thresholds for characters
veryFriendly = 50
friendly = 40
neutral = 30
unFriendly = 20
veryUnFriendly = 10
insane = 5

#names and related things
char1Name = "Sarah"
sameName = False

#character dictionaries
#these hold base values
SarahDictBaseValues = {
  "morality": 150,
  "antagonize": 0,
  "antThresh": veryFriendly,
  "charName": char1Name
}

#these hold actual working values
SarahDict = {
  "morality": 150,
  "antagonize": 0,
  "antThresh": veryFriendly,
  "charName": char1Name
}

#functions
def UpdateCharDict(morality, antagonize, antThresh):
  #print(SarahDict)
  #time.sleep(5)
  if SarahDict["morality"] != morality:
    SarahDict["morality"] != morality
    
  if SarahDict["antagonize"] != antagonize:
    SarahDict["antagonize"] = antagonize
    
  if SarahDict["antThresh"] != antThresh:
    SarahDict["antThresh"] = antThresh
  #time.sleep(5)
  #print(SarahDict)

#intialize char dicts in case values are broken somehow
def InitializeCharDicts():
  #char 1
  UpdateCharDict(SarahDictBaseValues["morality"], SarahDictBaseValues["antagonize"], SarahDictBaseValues["antThresh"])
