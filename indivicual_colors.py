from FluidicLib import *
import controller
import constants
#loadpath = "./final_fixture_description_localhost.json"
loadpath= "./final_fixture_description.json"
fluidicLib = FluidicLib(loadpath)
strands = fluidicLib.strands

color_map = {
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "magenta": (255, 0, 255),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0),
    "off": (0, 0, 0)
}

while True:
	experiment = input("Choose Strand:").upper()
	experiment = getattr(constants,experiment)
	experiment = fluidicLib.strands[experiment]


	partickle = input("Choose Partcikle:").upper()
	partickle = getattr(constants,partickle)

	color_input = input("Enter Color (blue, white, magenta, green, yellow, off): ").strip().lower()
	color_input = color_map[color_input]


	experiment[partickle].color.targetColor.set(*color_input)
	experiment[partickle].color.setOn()
	fluidicLib.controllers.updateLedsColors(strands)
	fluidicLib.controllers.updateArtnet()

#	for i, pod in enumerate(strands[experiment]):
 #   		print(f"Pod {i} - targetColor:", pod.color.targetColor.r, pod.color.targetColor.g, pod.color.targetColor.b)

