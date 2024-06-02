# from pod import *
# from abc import ABC, abstractmethod


# class BaseAnimationChain(ABC):
# 	def __init__(self):
# 		self.__repeatCounter = 0
# 		self.__repeat = 0
# 		self.__onEndCallbacks = []
# 		self.__nextAnimations = None



		
# 	def resetRepeats(self):
# 		self.__repeatCounter = 0

# 	def repeatOnce(self):
# 		self.__repeat = 1

# 	def repeatTimes(self, times: int):
# 		self.__repeat = times

# 	def repeatInfinite(self):
# 		self.__repeat = -1

# 	@abstractmethod
#     def __tryRepeat(self):
#         pass

# 	def __shouldTryRepeat(self):
# 		if self.__repeatCounter < self.__repeat  or self.__repeat < 0:
# 			self.__repeatCounter += 1
# 			return True
# 		return False
		
# 	def onEnd(self, callback):
# 		self.__onEndCallbacks.append(callback)

# 	def setNextAnimation(self, nextAnimations):
# 		self.nextAnimations = nextAnimations

# 	def __startNext(self):
# 		self.__tryStartNext(self.nextAnimations)
# 		# if type(self.nextAnimations) is None:
# 		# 	return

# 		# if isinstance(self.nextAnimations, list):
# 		# 	for n in self.nextAnimations:
# 		# 		n.start()
# 		# elif isinstance(self.nextAnimations, PodAnimation):
# 		# 	self.nextAnimations.start()
# 		# else:
# 		# 	start = getattr(self.nextAnimations, "start", None)
# 		# 	if callable(start):
# 		# 		self.nextAnimations.start()

# 	def __tryStartNext(self, _next):
# 		if type(_next) is None:
# 			return

# 		if isinstance(_next, list):
# 			for n in _next:
# 				self.__tryStartNext(n)
# 				# n.start()
# 		elif isinstance(_next, (PodAnimationChain, PodAnimation)):
# 			_next.start()
# 		else:
# 			start = getattr(_next, "start", None)
# 			if callable(start):
# 				_next.start()


# 	def __onEndCallback(self):
# 		self.__tryRepeat()

# 		for c in self.__onEndCallbacks:
# 			if(callable(c)):
# 				c(self)

# 		self.__startNext()


# class PodAnimationChain(BaseAnimationChain):
# 	def __init__(self, elementsToChain:list,  fadeInDuration = BLINK_DEFAULT_FADE_IN_DURATION, onDuration = BLINK_DEFAULT_ON_DURATION, fadeOutDuration = BLINK_DEFAULT_FADE_OUT_DURATION, startDelay = 0.0):
# 		# self.__elementsToChain = elementsToChain

# 		self.__chain = []


# 		for element in elementsToChain:
# 			self.append(element, fadeInDuration, onDuration, fadeOutDuration , startDelay)
			

# 		# for i in range(len(self.__chain)):
# 		# 	if i == 0:
# 		# 		continue
# 		# 	self.__chain[i-1].setNextAnimation(self.__chain[i])

# 	def __setNextForLast(self):
# 		n = len(self.__chain) - 1
# 		if n > 0 :
# 			self.__chain[n-1].setNextAnimation(self.__chain[n])

# 	def append(self, element,  fadeInDuration = BLINK_DEFAULT_FADE_IN_DURATION, onDuration = BLINK_DEFAULT_ON_DURATION, fadeOutDuration = BLINK_DEFAULT_FADE_OUT_DURATION, startDelay = 0.0):
# 		if isinstance(element, Pod):
# 			self.__chain.append(PodAnimation(element, fadeInDuration, onDuration, fadeOutDuration , startDelay))
# 			self.__setNextForLast()
# 		elif isinstance(element, PodAnimation):
# 			self.__chain.append(element)
# 			self.__setNextForLast()
# 		# else isinstance(element, list):


# 	def start(self):
# 		if len(self.__chain) >0 :
# 			return self.__chain[0].start()

# 	def getAsString(self, indentation = "") -> str:
# 		if len(self.__chain) >0 :
# 			return self.__chain[0].getAsString(indentation)
# 		return ""

# 	def getLast(self):
# 		n = len(self.__chain)
# 		if n >0 :
# 			return self.__chain[n - 1]
# 		return None

# 	def __tryRepeat(self):
# 		if __shouldTryRepeat():
# 			return
		
# 	# def repeatInfinite(self):
# 	# 	cn = len(self.__chain)
# 	# 	if cn > 1:
# 	# 		self.__chain[cn-1].setNextAnimation(self.__chain[0])

# 	# def onEndCallback(self):
# 	# 	self.__tryRepeat()

# 	# 	for c in self.__onEndCallbacks:
# 	# 		if(callable(c)):
# 	# 			c()
		
# 	# 	self.__startNext()





# class PodAnimation(BaseAnimationChain):
# 	def __init__(self, pod:Pod, fadeInDuration = BLINK_DEFAULT_FADE_IN_DURATION, onDuration = BLINK_DEFAULT_ON_DURATION, fadeOutDuration = BLINK_DEFAULT_FADE_OUT_DURATION, startDelay = 0.0):
# 		super().__init__()

# 		self.pod = pod
# 		self.fadeInDuration = fadeInDuration
# 		self.onDuration = onDuration
# 		self.fadeOutDuration = fadeOutDuration
# 		self.startDelay = startDelay
# 		# self.__repeat = 0
# 		# self.__repeatCounter = 0
# 		# self.__onEndCallbacks = []





# 	def start(self):
# 		self.resetRepeats()
# 		self.__blink()
	
		
		
# 	def getAsString(self, indentation = "") -> str:
# 		s = indentation + self.pod.name + " c\n"
# 		if isinstance(self.nextAnimations, (PodAnimation, PodAnimationChain)):
# 			s += indentation + "|\n" + self.nextAnimations.getAsString(indentation)
# 		elif isinstance(self.nextAnimations, list):
# 			for n in self.nextAnimations:
# 				s += n.getAsString(indentation + "  ") + " a\n"
# 		elif self.nextAnimations is not None:
# 			print("PodAnimation name: %s, wrong next type: %s" % (self.pod.name, str(type(self.nextAnimations))))

# 		return s;

# 	def stop(self):
# 		self.pod.setOff()
		

# 	# def repeatOnce(self):
# 	# 	self.__repeat = 1
# 	# 	pass

# 	# def repeatTimes(self, times: int):
# 	# 	self.__repeat = times
# 	# 	pass

# 	# def repeatInfinite(self):
# 	# 	self.__repeat = -1
# 	# 	pass

# 	def __tryRepeat(self):
# 		if __shouldTryRepeat():
# 			self.__blink()
# 		# if self.__repeatCounter < self.__repeat  or self.__repeat < 0:
# 		# 	self.__blink()
# 		# 	self.__repeatCounter += 1


# 	def __blink(self):
# 		print("PodAnimation %s blink" % (self.pod.name))
# 		self.pod.blink(self.fadeInDuration, self.onDuration, self.fadeOutDuration, self.startDelay , self.__onEndCallback)


	


# 	# def __onEndCallback(self):
# 	# 	self.__tryRepeat()

# 	# 	for c in self.__onEndCallbacks:
# 	# 		if(callable(c)):
# 	# 			c(self)

# 	# 	self.__startNext()

