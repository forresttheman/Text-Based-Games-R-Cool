import time
import characters
from characters import *

#player stats/variables
morality = 100 #0 is completely murderous, uncaring, 200 is angelic and wonderful, 100 is neutral
antagonize = 0 
#adds up, if passes threshold, character gets mad at you. Have diff aggression levels for repeated bad/good actions

#antagonize thresholds for characters
veryFriendly = 50
friendly = 40
neutral = 30
unFriendly = 20
veryUnFriendly = 10
insane = 5

#char lists
characterList = []
char1MoralitySaved = []

#char specific lists
SarahList = []

#names and related things
char1Name = "Sarah"
sameName = False

#character dictionaries
#these hold working values and start out with base values
SarahDict = {
  "morality": 150,
  "antagonize": 0,
  "antThresh": veryFriendly,
  "charName": char1Name
}

#functions
#do i even need this function?
def charFrame(charDict, charList):
  morality = charDict["morality"]
  antagonize = charDict["antagonize"]
  antThresh = charDict["antThresh"]
  charName = charDict["charName"]

  charList.append(morality)
  charList.append(antagonize)
  charList.append(antThresh)
  charList.append(charName)

#call this to change any values in the character's dictionary
def UpdateCharDict(dict, moralityf, antagonizef, antThreshf):
  #print(dict)
  #time.sleep(5)
  
  if moralityf != 0:
    if dict["morality"] != moralityf:
      dict["morality"] = moralityf
  
  if antagonizef != 0:
    if dict["antagonize"] != antagonizef:
      dict["antagonize"] = antagonizef

  if antThreshf != 0:
    if dict["antThresh"] != antThreshf:
      dict["antThresh"] = antThreshf
      
  #time.sleep(5)
  #print(dict)

#intialize char dicts in case values are broken somehow
def InitializeCharDicts():
  #char 1
  UpdateCharDict(SarahDict, 0, 0, 0)
