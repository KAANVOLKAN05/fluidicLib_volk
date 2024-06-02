# from pod import *
# from abc import ABC, abstractmethod

from pod import *


from stringHelpers import *


CHAIN_TYPE_SERIAL = 0
CHAIN_TYPE_PARALLEL = 1



class Repeatable:
	def __init__(self):
		self.__repeatCounter = 0
		self.__repeat = 0
		

	def resetRepeats(self):
		self.__repeatCounter = 0

	def repeatOnce(self):
		self.__repeat = 1

	def repeatTimes(self, times: int):
		self.__repeat = times

	def repeatInfinite(self):
		self.__repeat = -1
	
    # def __tryRepeat(self):
        # pass

	def shouldTryRepeat(self):
		if self.__repeatCounter < self.__repeat  or self.__repeat < 0:
			self.__repeatCounter += 1
			return True
		return False



class Chain(Repeatable):
	def __init__(self, elements, parentChain = None):
		self.__chain = []
		self.type = 0
		self.parentChain = parentChain
		super().__init__()
		
		

		for element in elements:
			if isinstance(element, Pod):
				self.__chain.append(ChainLink(element, self))
			elif isinstance(element, (Chain, ChainLink)):
				element.setParent(self)
				self.__chain.append(element)
			elif isinstance(element, list):
				# last = getLast()
				self.__chain.append(Chain(element, self))

			elif isinstance(element, tuple):
				if len(element) != 3:
					print("Chain ERROR: when using a tuple (parallel linking) it must have 3 elements " )
					return
				
				self.__chain.append(Chain(element, self))
			else:
				print("Chain ERROR: wrong type of element passed: %s" % type(element))
		
		if isinstance(elements, list):
			self.type = CHAIN_TYPE_SERIAL
			# if len(self.__chain) > 1:
			# 		lastInd = len(self.__chain) - 1
			# 		self.__chain[lastInd - 1].setNext(self.__chain[lastInd].getFirst())
			for i in range(1, len(elements)):
				self.__chain[i - 1].setNext(self.__chain[i].getFirst())
		elif isinstance(elements, tuple):
			self.type = CHAIN_TYPE_PARALLEL
			for i in range(1,len(elements)):
				# self.setNext(self.__chain[i].getFirst())
				self.__chain[0].setNext(self.__chain[i].getFirst())
		else:
			print("Chain ERROR: you should only pass a list (array) or tuple as the constructor arguments. passed type is %s"% (type(elements)) )
			return

	def setParent(self):

	def setNext(self, __next):
		if self.type == CHAIN_TYPE_PARALLEL:
			if len(self.__chain) > 0:
				self.__chain[0].setNext(__next)
		elif self.type == CHAIN_TYPE_SERIAL:
			last = self.getLast()
			if last is not None:
				last.setNext(__next)

	def getFirst(self):
		if len(self.__chain) > 0 :
			return self.__chain[0]
		return None

	def getLast(self):
		n = len(self.__chain)
		if n >0 :
			return self.__chain[n - 1]
		return None

	def start(self):
		self.resetRepeats()
		first = self.getFirst()
		if first is not None:
			first.start()

	def linkEnded(self, link):
		print("linkEnded")
		if link is None:
			return
		# print(self.getLast())
		if self.getLast() is link:
			if self.parentChain is not None:
				self.parentChain.linkEnded(self)

			if self.shouldTryRepeat():
				if self.getFirst() is not None:
					self.getFirst().start()


	
	def getStructuredName(self):
		if self.type == CHAIN_TYPE_PARALLEL:
			if len(self.__chain) != 3:
				print("ERROR getStructuredName(): number of elements is not 3")
			else:
				s0 = self.__chain[0].getStructuredName()
				s1 = self.__chain[1].getStructuredName()
				s2 = self.__chain[2].getStructuredName()
				
				n = joinStringsByLine( makeSeparator(len(s0[0]), s1[1], s1[2], ["   ", " - ", " | "]) , s1[0]) + "\n"
				n = n + s0[0] + " +\n"
				n = n + joinStringsByLine( makeSeparator(len(s0[0]), s2[1], s2[2], [" | ", " - ", "   "]) , s2[0])

				return (n, getStringHeight(n), s1[1])

		elif self.type == CHAIN_TYPE_SERIAL:
			s = ""
			for c in self.__chain:
				sn = c.getStructuredName()
				if sn[2] > 0:
					s = "\n"*sn[2] + s
				s = joinStringsByLine(s, sn[0], " - ")
			return (s, getStringHeight(s), 0)

		return ("", 0, 0)

	def printStructure(self):
		print(self.getStructuredName()[0])
	
	# def printNameNext(self):
	# 	for c in self.__chain:
	# 		if isinstance(c, ChainLink):
	# 			print(c.getName())
	# 		else:
	# 			c.printNameNext()


class ChainLink(Repeatable):
	def __init__(self, pod:Pod, parentChain = None,  fadeInDuration = BLINK_DEFAULT_FADE_IN_DURATION, onDuration:float = BLINK_DEFAULT_ON_DURATION, fadeOutDuration:float = BLINK_DEFAULT_FADE_OUT_DURATION, startDelay:float = BLINK_DEFAULT_START_DELAY):
		self.fadeInDuration  = fadeInDuration 
		self.onDuration = onDuration
		self.fadeOutDuration = fadeOutDuration
		self.startDelay = startDelay

		self.pod = pod
		self.__next = []
		self.parentChain = parentChain
		# self.color = FadingColor(Color())

		super().__init__()

	def getStructuredName(self):
		return (self.getName(), getStringHeight(self.getName()), 0)

	def printStructure(self):
		print(self.getStructuredName()[0])

	def getName(self):
		if self.pod :
			return self.pod.getName()
		else:
			return ""

	def setNext(self, __next):
		if __next is None:
			return
		if __next is self:
			print("ChainLink Warning: cant set next to self")
		if isinstance(__next, (ChainLink, Chain)):
			self.__next.append(__next)
		# elif isinstance(__next, list):
		# 	for n in __next:
		# 		self.setNext(n)
		else:
			print ("%s ChainLink::setNext(...) wrong type passed. It can only be objects of type ChainLink. "% self.getName() )
		

	def __startNext(self):
		for n in self.__next:
			n.start()

	def onEndCallback(self):
		print ( "%s end callback" % self.getName())
		if self.parentChain is not None:
			self.parentChain.linkEnded(self)

		if self.shouldTryRepeat():
			self.__blink()
		self.__startNext()

	def getFirst(self):
		return self

	def getLast(self):
		return self

	def start(self):
		self.resetRepeats()
		print( "%s start" % self.getName())
		self.__blink()
	
	def __blink(self):
		# blink(fadeInDuration = BLINK_DEFAULT_FADE_IN_DURATION, onDuration:float = BLINK_DEFAULT_ON_DURATION, fadeOutDuration:float = BLINK_DEFAULT_FADE_OUT_DURATION, startDelay = 0.0, onEndCallback = None):
		self.pod.blink(self.fadeInDuration, self.onDuration, self.fadeOutDuration, self.startDelay, self.onEndCallback)
		# self.color.fadeInOut
	

	

if __name__ == "__main__":

	import time
	from helpers import *

	last_update_time = time.time()

	def update():
		t = time.time()
		global last_update_time
		dt = t - last_update_time
		last_update_time = t
		tween.update(dt)

# link0 = Chain(["0"])#, "1", "2"])	
# links = []
# for i in range(3, 6) :	
# 	links.append(Chain([str(i)])) 


# for l in links:
# 	link0.setNext(l)	

# link0.start()


	chain = Chain((["1", "11", "111"], ("2", ("3", "4", "5"), ("6","7","8")), "9"))
# chain = Chain(("1", ("2", ("3", "4", "5"), ("6","7","8")), "9"))
# chain.printStructure()
# chain = Chain(("1","2\n3\n4\n6","7\n8\n9"))
	chain.printStructure()
# print(chain.getStructuredName()[0])
# chain = Chain(["1", "2", "3", ["4", "5", "6"]])
# chain = Chain(["1", "2", "3", ["4", "5", "6"]])

	chain.start() 

	repeatEvery(1.0/30, update)
