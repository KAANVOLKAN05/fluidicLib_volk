from pod import *


class PodAnimationChain:
	def __init__(self, elementsToChain:list):
		# self.__elementsToChain = elementsToChain
		self.__chain = []
		for element in elementsToChain:
			self.append(element)
			

		# for i in range(len(self.__chain)):
		# 	if i == 0:
		# 		continue
		# 	self.__chain[i-1].setNextAnimation(self.__chain[i])

	def __setNextForLast(self):
		n = len(self.__chain) - 1
		if n > 0 :
			self.__chain[n-1].setNextAnimation(self.__chain[n])

	def append(self, element):
		if isinstance(element, Pod):
			self.__chain.append(PodAnimation(element))
			self.__setNextForLast()
		elif isinstance(element, PodAnimation):
			self.__chain.append(element)
			self.__setNextForLast()
		# else isinstance(element, list):


	def start(self):
		if len(self.__chain) >0 :
			return self.__chain[0].start()

	def getAsString(self, indentation = "") -> str:
		if len(self.__chain) >0 :
			return self.__chain[0].getAsString(indentation)
		return ""

	def getLast(self):
		n = len(self.__chain)
		if n >0 :
			return self.__chain[n - 1]
		return None





class PodAnimation:
	def __init__(self, pod:Pod, fadeInDuration = BLINK_DEFAULT_FADE_DURATION, onDuration = BLINK_DEFAULT_ON_DURATION, fadeOutDuration = BLINK_DEFAULT_FADE_DURATION, startDelay = 0.0):
		self.pod = pod
		self.nextAnimations = None
		self.fadeInDuration = fadeInDuration
		self.onDuration = onDuration
		self.fadeOutDuration = fadeOutDuration
		self.startDelay = startDelay
		self.__repeat = 0
		self.__repeatCounter = 0

	def setNextAnimation(self, nextAnimations):
		self.nextAnimations = nextAnimations


	def start(self):
		self.__repeatCounter = 0
		self.__blink()
		# if isinstance(self.pod, Pod):
		
		
	def getAsString(self, indentation = "") -> str:
		s = indentation + self.pod.name + " c\n"
		if isinstance(self.nextAnimations, (PodAnimation, PodAnimationChain)):
			s += indentation + "|\n" + self.nextAnimations.getAsString(indentation)
		elif isinstance(self.nextAnimations, list):
			for n in self.nextAnimations:
				s += n.getAsString(indentation + "  ") + " a\n"
		elif self.nextAnimations is not None:
			print("PodAnimation name: %s, wrong next type: %s" % (self.pod.name, str(type(self.nextAnimations))))

		return s;

	def stop(self):
		self.pod.setOff()
		

	def repeatOnce(self):
		self.__repeat = 1
		pass

	def repeatTimes(self, times: int):
		self.__repeat = times
		pass

	def repeatInfinite(self):
		self.__repeat = -1
		pass

	def __tryRepeat(self):
		if self.__repeatCounter < self.__repeat  or self.__repeat < 0:
			self.__blink()
			self.__repeatCounter += 1


	def __blink(self):
		print("PodAnimation %s blink" % (self.pod.name))
		self.pod.blink(self.fadeInDuration, self.onDuration, self.fadeOutDuration, self.startDelay , self.onEndCallback)

	def onEndCallback(self):
		self.__tryRepeat()

		if type(self.nextAnimations) is None:
			return

		if isinstance(self.nextAnimations, list):
			for n in self.nextAnimations:
				n.start()
		elif isinstance(self.nextAnimations, PodAnimation):
			self.nextAnimations.start()
		else:
			start = getattr(self.nextAnimations, "start", None)
			if callable(start):
				self.nextAnimations.start()

