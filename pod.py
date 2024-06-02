
from color import *

import json
import random

BLINK_DEFAULT_ON_DURATION = 0.0
BLINK_DEFAULT_FADE_IN_DURATION = 3.0
BLINK_DEFAULT_FADE_OUT_DURATION = 3.0
BLINK_DEFAULT_START_DELAY = 0.0

POD_TYPE_FLOWER = 1
POD_TYPE_POD = 2


class Pod:
  def __init__(self, name:str, color: Color, podType:int, ledIDs:list):
    self.__name = name
    self.podType = podType
    self.color = FadingColor(color)
    self.ledIDs = ledIDs
    
  def setOff(self):
    self.color.setOff()

  def setOn(self):
    self.color.setOn()

  def blink(self, fadeInDuration:float = BLINK_DEFAULT_FADE_IN_DURATION, onDuration:float = BLINK_DEFAULT_ON_DURATION, fadeOutDuration:float = BLINK_DEFAULT_FADE_OUT_DURATION, startDelay = BLINK_DEFAULT_START_DELAY, onEndCallback = None):
    self.color.fadeInOut(fadeInDuration, onDuration, fadeOutDuration, startDelay, onEndCallback)

  def setOnWhite(self):
    self.color.setOnWhite()
  
  def getName(self):
    return self.__name

def toPodType(podType:str):
  if podType == "pod":
    return POD_TYPE_POD
  elif podType == "flower":
    return POD_TYPE_FLOWER
  else:
    print("toPodType(type:str)  failed. passed " + podType)
    return 0

def loadPods(loadPath):
  strands = [{} for i in range(4)]
  f = open(loadPath)
  j_data = json.load(f)
  for comp in j_data['InstallationComponents']:
    ind = comp["groupID"]
    strands[ind] = [i for i in range(len(comp["fixtures"]))]
    i = 0
    for pod in comp["fixtures"]:
      c = i%3
      i+=1
      color = Color()
      #this is an ugly hack to set the colors for each strand.
      if(ind == 0):
        color.set(255,0,255)#magenta
      elif ind == 1:
        color.set(0,0,255)#blue
      elif ind == 2:
        color.set(0,255,0)#green
      elif ind == 3:
        color.set(255,255,0)#yellow
      
      strands[ind][pod["fixtureID"]] = Pod(pod["fixtureName"], color, toPodType(pod["fixtureType"]), pod["LEDs"])
  f.close()
  return strands
