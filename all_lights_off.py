from FluidicLib import *


#loadpath = "./final_fixture_description_localhost.json"
loadpath= "./final_fixture_description.json"
fluidicLib = FluidicLib(loadpath)

alice = fluidicLib.strands[0]

atlas = fluidicLib.strands[1]

cms = fluidicLib.strands[2]

lhcb = fluidicLib.strands[3]

#Be happy
for pod in alice:
	pod.setOff()

for pod in atlas:
	pod.setOff()

for pod in cms:
        pod.setOff()

for pod in lhcb:
        pod.setOff()
