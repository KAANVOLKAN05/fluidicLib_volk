
from FluidicLib import *
import constants

#loadpath = "./final_fixture_description_localhost.json"
loadpath= "./final_fixture_description.json"
fluidicLib = FluidicLib(loadpath)


while True:

	experiment = input("Choose Strand:")
	experiment = getattr(constants,experiment)
	experiment = fluidicLib.strands[experiment]


	partickle = input("Choose Partcikle:")
	partickle = getattr(constants,partickle)

	switch = input("1 to turn on, 0 to turn off:")
	switch = int(switch)
	if switch == 1:
		experiment[partickle].setOn()
	elif switch == 0:
		experiment[partickle].setOff()
