from pod import *
from constants import *
from helpers import *
from stupidArtnet import StupidArtnet
import json
from led import *
from animation import *



artnet = {}
leds = []
# strands = [{} for i in range(4)]
strands = []


class Artnet:
	def __init__(self, ipAddress, controllerId, description):
		self.ipAddress = ipAddress
		self.controllerId = controllerId
		self.description = description
		self.controllers = dict()
		self.data = dict()


	def addUniverse(self, universe):
		self.controllers[str(universe)] = StupidArtnet(self.ipAddress, universe, 512, 30, True, True)
		print(self.controllers[str(universe)])
		self.data[str(universe)] = bytearray(512)
		for i in range(512):
			self.data[str(universe)][i] = 0

	def start(self):
		for u in self.controllers.keys():
 			self.controllers[u].start()

	def stop(self):
		for u in self.controllers.keys():
 			self.controllers[u].stop()

	def updateData(self):
		for l in leds:
			if l.controllerId == self.controllerId:
				l.updateData(self.data[str(l.universe)])

		for u in self.controllers.keys():
			self.controllers[u].set(self.data[u])
			self.controllers[u].show()


	def printBuffers(self):
		for u in self.controllers.keys():
			self.controllers[u].see_buffer()
		







def loadControllers(loadPath):
	f = open(loadPath)
	j_data = json.load(f)
	for ctrl in j_data['Controllers']:
		if ctrl["ControllerIP"] == "":
			continue
		artnet[str(ctrl["ControllerID"])] = Artnet(ctrl["ControllerIP"], ctrl["ControllerID"], ctrl["Description"])

		# the following is to make a list of the universes without repeating these. maybe there is a smarter way to do such
		universesSet = set()
		for led in leds:
			if led.controllerId == ctrl["ControllerID"]:
				universesSet.add(led.universe)
		universes = []
		for u in universesSet:
			universes.append(u)

		universes.sort()
		for u in universes:
			artnet[str(ctrl["ControllerID"])].addUniverse(u)

		print("Controller %d universes: " % ctrl["ControllerID"])
		print(universes)

	f.close()


last_update_time = time.time()

def updateLedsColors():
	for strand in strands:
		for pod in strand:
			for i in pod.ledIDs:
				leds[i].setColor(pod.color.get())

    

def start():
	for k in artnet.keys():
		artnet[k].start()
def stop():
	for k in artnet.keys():
		artnet[k].stop()


def updateArtnet():
	for k in artnet.keys():
		artnet[k].updateData()


def update():
	t = time.time()
	global last_update_time
	dt = t - last_update_time
	last_update_time = t
	tween.update(dt)
	updateLedsColors()
	updateArtnet()
    



# loadpath ="./final_fixture_description_localhost.json"
loadpath ="./final_fixture_description.json"
loadPods(loadpath)
leds = loadLeds(loadpath)
strands = loadPods(loadpath)
loadControllers(loadpath)

# for strand in strands:
# 		for pod in strand:
# 			pod.blink(10, 4, 10)

# for()


# chain0 = PodAnimationChain(strands[0])
# chain1 = PodAnimationChain(strands[1])
# chain2 = PodAnimationChain(strands[2])
# chain3 = PodAnimationChain(strands[3])
# chain0.start()
# chain1.start()
# chain2.start()
# chain3.start()

podAnimations = []

for s in strands:
	for p in s:
		# p.setOn()
		# p.setOnWhite()
		podAnimations.append(PodAnimation(p));
		podAnimations[len(podAnimations) -1].repeatInfinite()
		podAnimations[len(podAnimations) -1].start()

# l = chain0.getLast()
# if l is not None:
# 	l.setNextAnimation([chain1, chain2])

# print(chain0.getAsString())






# start()

repeatEvery(1.0/30, update)

