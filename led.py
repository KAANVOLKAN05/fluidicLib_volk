from color import *

import json


class LED:
	def __init__(self, startIndex:int, size: int, universe:int, controllerId:int):
		self.size = size
		self.universe = universe
		self.controllerId = controllerId
		self.startIndex = startIndex
		self.color = Color()

	def updateData(self, data):
		for i in range(self.size):
			data[self.startIndex + (i*3)] = round(self.color.r)
			data[self.startIndex + (i*3) + 1] = round(self.color.g)
			data[self.startIndex + (i*3) + 2] = round(self.color.b)

	def setColor(self, c:Color):
		self.color.set(c.r, c.g, c.b)


def typeToSize(ledType:str):
	if ledType == "8_LED_ring":
		return 8
	elif ledType == "12_LED_ring":
		return 12
	else:
		print("typeToSize() failed . passed: " + ledType)
	return 0

def loadLeds(loadPath):
	leds = []
	f = open(loadPath)
	j_data = json.load(f)
	leds = [{} for i in range(len(j_data['LEDDevices']))]
	for led in j_data['LEDDevices']:
		leds[led["LEDGroupID"]] = LED(led["LedIDs"][0], typeToSize(led["type"]), led["universe"], led["controllerID"])
	f.close()

	return leds



if __name__ == "__main__":

	loadLeds("./final_fixture_description.json")
	# loadpath ="./final_fixture_description_localhost.json"


    