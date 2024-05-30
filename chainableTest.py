# from pod import *
# from abc import ABC, abstractmethod
import time
from color import *

from helpers import *




class BaseChainable():
	def __init__(self, name):
		self.name = name
		# self.__repeatCounter = 0
		# self.__repeat = 0
		# self.__endCallbacks = []
		self.__next = []

	# def resetRepeats(self):
	# 	self.__repeatCounter = 0

	# def repeatOnce(self):
	# 	self.__repeat = 1

	# def repeatTimes(self, times: int):
	# 	self.__repeat = times

	# def repeatInfinite(self):
	# 	self.__repeat = -1

	# @abstractmethod
    # def __tryRepeat(self):
    #     pass

	# def __shouldTryRepeat(self):
	# 	if self.__repeatCounter < self.__repeat  or self.__repeat < 0:
	# 		self.__repeatCounter += 1
	# 		return True
	# 	return False

	# @abstractmethod
	# def __startNext(self):
	# 	pass

	# @abstractmethod
	# def __onEndCallback(self):
	# 	pass

	# def onEnd(self, callback):
	# 	self.__endCallbacks.append(callback)

	def setNext(self, __next):
		self.__next.append(__next)

	def __startNext(self):
		# self.__tryStartNext(self.__next)
		# if type(self.nextAnimations) is None:
		# 	return

		# if isinstance(self.nextAnimations, list):
		# 	for n in self.nextAnimations:
		# 		n.start()
		# elif isinstance(self.nextAnimations, PodAnimation):
		# 	self.nextAnimations.start()
		# else:
		# 	start = getattr(self.nextAnimations, "start", None)
		# 	if callable(start):
		# 		self.nextAnimations.start()

	# def __tryStartNext(self, _next):
		# if type(_next) is None:
			# return

		# if isinstance(_next, list):
		for n in self.__next:
				# self.__tryStartNext(n)
			n.start()
		# elif isinstance(_next, (Chain, ChainLink)):
		# 	_next.start()
		# else:
		# 	start = getattr(_next, "start", None)
		# 	if callable(start):
		# 		_next.start()


	def onEndCallback(self):
		print ( "%s end callback" % self.name)
		# self.__tryRepeat()

		# for c in self.__endCallbacks:
		# 	if(callable(c)):
		# 		c(self)

		self.__startNext()

	

class Chain(BaseChainable):
	def __init__(self, elementsToChain):
		# BaseChainable.__init__(self)
		super().__init__("Chain")
		self.__chain = []

		# self.append(elementsToChain)
		for element in elementsToChain:
			self.append(element)
			
	def __setNextForLast(self):
		n = len(self.__chain) - 1
		if n > 0 :
			self.__chain[n-1].setNext(self.__chain[n])

	def append(self, element, last = None):
		# if last == None:
			# last = self.getLast()

		if isinstance(element, str):
			self.__chain.append(ChainLink(element, self))
			if last is not None:
				last.setNext(self.getLast())

		elif isinstance(element, list):
			for e in element:
				self.append(e, last)
			# self.append(Chain(element))
			# if last is not None:
			# 	last.setNext(self.getLast())

				# self.__setNextForLast()
			# for e in element:
			# 	self.append(e)
			# 	self.__setNextForLast()
		elif isinstance(element, BaseChainable):
			self.__chain.append(element)
			if last is not None:
				last.setNext(self.getLast())
			# self.__setNextForLast()
		# else isinstance(element, list):


	def start(self):
		if len(self.__chain) >0 :
			self.startTime = time.time()
			return self.__chain[0].start()


	def getLast(self):
		n = len(self.__chain)
		if n >0 :
			return self.__chain[n - 1]
		return None

	def linkEnded(self, link):
		print("linkEnded")
		# print(link)
		if link is None:
			return
		# print(self.getLast())
		if self.getLast() is link:
			self.onEndCallback()

	# def __tryRepeat(self):
	# 	if __shouldTryRepeat():
	# 		return
	
		



class ChainLink(BaseChainable):
	def __init__(self, name, parentChain = None):
		super().__init__(name)
		self.parentChain = parentChain
		# BaseChainable.__init__(self)
		
		self.color = FadingColor(Color())


	def start(self):
		# self.resetRepeats()
		self.startTime = time.time()
		print( "%s start" % self.name)
		self.__blink()
	
		
	# def __tryRepeat(self):
	# 	if __shouldTryRepeat():
	# 		self.__blink()

	def __endCallback(self):
		print ("__endCallback")
		# print (self.parentChain)
		if self.parentChain is not None:
			self.parentChain.linkEnded(self)

		self.onEndCallback()

	def __blink(self):
		self.color.fadeInOut(0.1, 0.1, 0.1, 0, self.__endCallback)
		# self.startTime = 
		# time.sleep(2.5)
		# self.onEndCallback()

	def update(self):
		pass



last_update_time = time.time()
		


def update():
	t = time.time()
	global last_update_time
	dt = t - last_update_time
	last_update_time = t
	tween.update(dt)

link0 = Chain(["0"])#, "1", "2"])	
links = []
for i in range(3, 6) :	
	links.append(Chain([str(i)])) 


for l in links:
	link0.setNext(l)	

link0.start()


# chain = Chain(["1", "2", "3", ["4", "5", "6"]])
# chain = Chain(["1", "2", "3", ["4", "5", "6"]])

# chain.start()

repeatEvery(1.0/30, update)
