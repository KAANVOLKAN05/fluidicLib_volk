from FluidicLib import *


#loadpath = "./final_fixture_description_localhost.json"
loadpath= "./final_fixture_description.json"
fluidicLib = FluidicLib(loadpath)


strands = fluidicLib.strands


for i, pod in enumerate(strands[ATLAS]):
    print(f"Pod {i} - targetColor:", pod.color.targetColor.r, pod.color.targetColor.g, pod.color.targetColor.b)
