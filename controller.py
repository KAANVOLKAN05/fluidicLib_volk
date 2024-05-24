from pod import *
from constants import *
from helpers import *
from stupidArtnet import StupidArtnet
import json
from led import *




# artnet = {}
# leds = []
# strands = []



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



	
	# def start(self):
	# 	for k in self.artnet.keys():
	# 		self.artnet[k].start()
	# def stop():
	# 	for k in self.artnet.keys():
	# 		self.artnet[k].stop()
	
	

	

# class FluidicLib:
# 	def __init__(self, loadpath):
# 		self.strands = loadPods(loadpath)
# 		self.controllers = FluidicControllers(loadpath)
# 		self.last_update_time = time.time()
		
# 		repeatEveryThreaded(1.0/30, self.update)

# 	def update(self):
# 		t = time.time()
		
# 		dt = t - self.last_update_time
# 		self.last_update_time = t
# 		tween.update(dt)
# 		self.controllers.updateLedsColors(self.strands)
# 		self.controllers.updateArtnet()
	    
# 	# def load(loadpath):
# 		# loadPods(loadpath)
# 		# leds = loadLeds(loadpath)
# 		# strands = loadPods(loadpath)
# 		# loadControllers(loadpath)

		
# 		# return strands
	

# 	def turnOnStrand(self, strandIndex):
# 		if strandIndex >= len(self.strands) or strandIndex < 0:
# 			print("turnOnStrand(strandIndex) index out of bounds. index == %d" % (strandIndex) )
# 			return

# 		for p in self.strands[strandIndex]:
# 			p.setOn()


# load("./final_fixture_description_localhost.json")
# load("./final_fixture_description.json")

# repeatEvery(1.0/30, update)

# for strand in strands:
# 		for pod in strand:
# 			pod.blink(10, 4, 10)

# for()

# for s in strands:
# 	podAnimations.append(PodAnimationChain(s));
# 		# podAnimations[len(podAnimations) -1].repeatInfinite()
# 	podAnimations[len(podAnimations) -1].start()




# for s in strands:
# 	for p in s:
# 		p.setOn()
# animations = []

# if __name__ == "__main__":
# 	loadpath = "./final_fixture_description_localhost.json"
# 	# loadpath ="./final_fixture_description.json"

# 	# loadPods(loadpath)
# 	# leds = loadLeds(loadpath)
# 	# strands = loadPods(loadpath)
# 	# loadControllers(loadpath)
# 	# repeatEveryThreaded(1.0/30, update)
# 	fluidicLib = FluidicLib(loadpath)

# 	# strands  = fluidicLib.strands

# 	# fluidicLib.turnOnStrand(0)
# 	# fluidicLib.turnOnStrand(strands[1])
# 	# fluidicLib.turnOnStrand(2)
# 	# fluidicLib.turnOnStrand(3)
# 	 # chain0 = PodAnimationChain(strands[0])

	 
# 	for s in fluidicLib.strands:
# 		chain1 = PodAnimationChain(s, 0.5, 0.5, 0.5)
# 		chain1.repeatInfinite()
# 		chain1.start()
# 		animations.append(chain1)

# 	# chain1 = PodAnimationChain(fluidicLib.strands[1])
# 	# chain2 = PodAnimationChain(strands[2])
# 	# chain3 = PodAnimationChain(strands[3])
# 	# chain0.start()
# 	# chain1.repeatInfinite()
# 	# chain1.start()


# # chain2.start()
# # chain3.start()



# # for s in strands:
# # 	for p in s:
# # 		p.setOn()
# # #		# p.setOnWhite()
# # 		podAnimations.append(PodAnimation(p));
# # 		podAnimations[len(podAnimations) -1].repeatInfinite()
# # 		podAnimations[len(podAnimations) -1].start()

# # l = chain0.getLast()
# # if l is not None:
# # 	l.setNextAnimation([chain1, chain2])

# # print(chain0.getAsString())






# # start()



