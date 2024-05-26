from pod import *
from constants import *
from helpers import *
from stupidArtnet import StupidArtnet
import json
from led import *




class Artnet:
	def __init__(self, leds, ipAddress, controllerId, description):
		self.ipAddress = ipAddress
		self.controllerId = controllerId
		self.description = description
		self.controllers = dict()
		self.data = dict()
		self.leds = leds


	def addUniverse(self, universe):
		self.controllers[str(universe)] = StupidArtnet(self.ipAddress, universe, 512, 30, True, True)
		print(self.controllers[str(universe)])
		self.data[str(universe)] = bytearray(512)
		for i in range(512):
			self.data[str(universe)][i] = 0

	def addUniverses(self, universes:list):
		for u in universes:
			self.addUniverse(u)

	def start(self):
		for u in self.controllers.keys():
 			self.controllers[u].start()

	def stop(self):
		for u in self.controllers.keys():
 			self.controllers[u].stop()

	def updateData(self):
		for l in self.leds:
			if l.controllerId == self.controllerId:
				l.updateData(self.data[str(l.universe)])

		for u in self.controllers.keys():
			self.controllers[u].set(self.data[u])
			self.controllers[u].show()


	def printBuffers(self):
		for u in self.controllers.keys():
			self.controllers[u].see_buffer()
		


class FluidicControllers:
	def __init__(self, loadpath):
		self.artnet = {}
		self.leds = []
		self.load(loadpath)
		
		
		

	def load(self, loadPath):
		self.leds = loadLeds(loadPath)

		f = open(loadPath)
		j_data = json.load(f)
		for ctrl in j_data['Controllers']:
			if ctrl["ControllerIP"] == "":
				continue
			self.artnet[str(ctrl["ControllerID"])] = Artnet(self.leds, ctrl["ControllerIP"], ctrl["ControllerID"], ctrl["Description"])
	
			# the following is to make a list of the universes without repeating these. maybe there is a smarter way to do such
			universesSet = set()
			for led in self.leds:
				if led.controllerId == ctrl["ControllerID"]:
					universesSet.add(led.universe)
			universes = []
			for u in universesSet:
				universes.append(u)
	
			universes.sort()
			# for u in universes:
			# 	artnet[str(ctrl["ControllerID"])].addUniverse(u)
			self.artnet[str(ctrl["ControllerID"])].addUniverses(universes)
	
			print("Controller %d universes: " % ctrl["ControllerID"])
			print(universes)
	
		f.close()


	def updateArtnet(self):
		for k in self.artnet.keys():
			self.artnet[k].updateData()
	
	def updateLedsColors(self, strands):
		for strand in strands:
			for pod in strand:
				for i in pod.ledIDs:
					self.leds[i].setColor(pod.color.get())




