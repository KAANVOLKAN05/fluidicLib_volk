from FluidicLib import *

animations = []


loadpath = "./final_fixture_description_localhost.json"
# loadpath ="./final_fixture_description.json"
# loadPods(loadpath)
# leds = loadLeds(loadpath)
# strands = loadPods(loadpath)
# loadControllers(loadpath)
# repeatEveryThreaded(1.0/30, update)
fluidicLib = FluidicLib(loadpath)
# strands  = fluidicLib.strands
# fluidicLib.turnOnStrand(0)
# fluidicLib.turnOnStrand(strands[1])
# fluidicLib.turnOnStrand(2)
# fluidicLib.turnOnStrand(3)
# chain0 = PodAnimationChain(strands[0])
 
for s in fluidicLib.strands:
	chain1 = PodAnimationChain(s, 0.5, 0.5, 0.5)
	chain1.repeatInfinite()
	chain1.start()
	animations.append(chain1)
# chain1 = PodAnimationChain(fluidicLib.strands[1])
# chain2 = PodAnimationChain(strands[2])
# chain3 = PodAnimationChain(strands[3])
# chain0.start()
# chain1.repeatInfinite()
# chain1.start()


# chain2.start()
# chain3.start()



# for s in strands:
# 	for p in s:
# 		p.setOn()
# #		# p.setOnWhite()
# 		podAnimations.append(PodAnimation(p));
# 		podAnimations[len(podAnimations) -1].repeatInfinite()
# 		podAnimations[len(podAnimations) -1].start()

# l = chain0.getLast()
# if l is not None:
# 	l.setNextAnimation([chain1, chain2])

# print(chain0.getAsString())






# start()



