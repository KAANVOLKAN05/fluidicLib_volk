
from FluidicLib import *


#loadpath = "./final_fixture_description_localhost.json"
loadpath= "./final_fixture_description.json"
fluidicLib = FluidicLib(loadpath)

strands = fluidicLib.strands

alice = fluidicLib.strands[0]

atlas = fluidicLib.strands[1]

cms = fluidicLib.strands[2]

lhcb = fluidicLib.strands[3]

#Be happy
for pod in alice:
	pod.color.targetColor.set(250,0,250)
	pod.setOn()
	fluidicLib.controllers.updateLedsColors(strands)
	fluidicLib.controllers.updateArtnet()

for pod in atlas:
	pod.color.targetColor.set(0,0,250)
	pod.setOn()
	fluidicLib.controllers.updateLedsColors(strands)
	fluidicLib.controllers.updateArtnet()

for pod in cms:
	pod.color.targetColor.set(0,250,0)
	pod.setOn()
	fluidicLib.controllers.updateLedsColors(strands)
	fluidicLib.controllers.updateArtnet()

for pod in lhcb:
	pod.color.targetColor.set(250,128,13)
	pod.setOn()
	fluidicLib.controllers.updateLedsColors(strands)
	fluidicLib.controllers.updateArtnet()
