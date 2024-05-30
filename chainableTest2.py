# from pod import *
# from abc import ABC, abstractmethod
import time
from color import *

# from helpers import *
from stringHelpers import *


# class ParallelChain:
# 	def __init__(self, elements):
# 		self.__chain = []	

# 		if len(elements) < 3:
# 			print("ParallelChain ERROR: passed elements must have at least 3 elements " )
# 			return
# 		self.__chain.append(elements)


CHAIN_TYPE_SERIAL = 0
CHAIN_TYPE_PARALLEL = 1



class Chain:
	def __init__(self, elements):
		self.__chain = []
		self.type = 0
		
		

		for element in elements:
			if isinstance(element, str):
				self.__chain.append(ChainLink(element))
			elif isinstance(element, list):
				# last = getLast()
				self.__chain.append(Chain(element))
			elif isinstance(element, tuple):
				if len(element) != 3:
					print("Chain ERROR: when using a tuple (parallel linking) it must have 3 elements " )
					return
				# last = getLast()
				self.__chain.append(Chain(element))
		
		
		if isinstance(elements, list):
			self.type = CHAIN_TYPE_SERIAL
			for i in range(1, len(elements)):
				self.__chain[i - 1].setNext(self.__chain[i].getFirst())
		if isinstance(elements, tuple):
			self.type = CHAIN_TYPE_PARALLEL
			for i in range(1,len(elements)):
				self.setNext(self.__chain[i].getFirst())
				# self.__chain[0].setNext(self.__chain[i].getFirst())
		else:
			print("Chain ERROR: you should only pass a list (array) or tuple as the constructor arguments")
			return

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
				s = joinStringsByLine(s, c.getStructuredName()[0], " - ")
			return (s, getStringHeight(s), 0)

		return ("", 0, 0)

	def printStructure(self):
		print(self.getStructuredName()[0])


class ChainLink():
	def __init__(self, name):
		self.name = name
		self.__next = []
		self.color = FadingColor(Color())

	def getStructuredName(self):
		return (self.name, getStringHeight(self.name), 0)

	def printStructure(self):
		print(self.getStructuredName()[0])


	def setNext(self, __next):
		if __next is None:
			return
		if __next is self:
			print("ChainLink Warning: cant set next to self")
		if isinstance(__next, ChainLink):
			self.__next.append(__next)
		# elif isinstance(__next, list):
		# 	for n in __next:
		# 		self.setNext(n)
		else:
			print ("%s ChainLink::setNext(...) wrong type passed. It can only be objects of type ChainLink. "% self.name )
		

	def __startNext(self):
		for n in self.__next:
			n.start()

	def onEndCallback(self):
		print ( "%s end callback" % self.name)
		self.__startNext()

	def getFirst(self):
		return self

	def getLast(self):
		return self

	def start(self):
	
		print( "%s start" % self.name)
		self.__blink()
	
	def __blink(self):
		self.color.fadeInOut(0.1, 0.1, 0.1, 0, self.onEndCallback)
	

	


last_update_time = time.time()
		


# def update():
# 	t = time.time()
# 	global last_update_time
# 	dt = t - last_update_time
# 	last_update_time = t
# 	tween.update(dt)

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

# repeatEvery(1.0/30, update)
