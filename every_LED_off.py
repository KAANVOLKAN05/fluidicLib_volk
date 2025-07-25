from FluidicLib import *
import constants

# Load fixture config
loadpath = "./final_fixture_description.json"
fluidicLib = FluidicLib(loadpath)
strands = fluidicLib.strands

# Step 1: Force all Pod colors to black
for strand in strands:
    for pod in strand:
        pod.color.targetColor.set(0, 0, 0)
        pod.color.setOff()          # Set fade level to 0.0
        pod.color.update()          # Apply fade to currentColor

# Step 2: Push Pod colors to LED objects
fluidicLib.controllers.updateLedsColors(strands)

# Step 3: Send data to Artnet
fluidicLib.controllers.updateArtnet()

print("✅ All Pod LEDs turned off.")

