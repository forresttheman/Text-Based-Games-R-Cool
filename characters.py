import time
import characters
import resources
from resources import *
from characters import *


#antagonize thresholds for characters
veryFriendly = 50
friendly = 40
neutral = 30
unFriendly = 20
veryUnFriendly = 10
insane = 5

#character names and related things
char1Name = "Sarah"
sameName = False

#character dictionaries
#these hold working values and start out with base values
Char1Dict = {
  "morality": 150,
  "antagonize": 0,
  "antThresh": veryFriendly,
  "charName": char1Name
}


###########
#FUNCTIONS#
###########

#call this to change any values in the character's dictionary
def UpdateCharDict(dict, moralityD, antagonizeD, antThreshD):
  #if the morality has been changed
  if moralityD != 0:
    #add the new morality to old morality and make that the new morality value in dictionary
    moralityNew = dict["morality"] + moralityD
    dict["morality"] = moralityNew

  #if the antagonize has changed
  if antagonizeD != 0:
    antagonizeNew = dict["antagonize"] + antagonizeD
    dict["antagonize"] = antagonizeNew

  if antThreshD != 0:
    #if the antagonize threshold is different
    if dict["antThresh"] != antThreshD:
      dict["antThresh"] = antThreshD

  #if exceeded antagonize threshold
  if dict["antagonize"] > dict["antThresh"]:
    resources.exAntThresh = True
    

#intialize char dicts (may be unnecessary, but it's good to make sure everything works)
def InitializeCharDicts():
  #char 1
  UpdateCharDict(Char1Dict, 0, 0, 0)
