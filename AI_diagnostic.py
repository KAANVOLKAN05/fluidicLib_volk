#This code is written by AI, I dont quite understand it, I was desperate for any solution so I asked GPT. 
#The result it returns apparently indicates all 0 bits. 
#So it confirms that the software side is alright for the most part.


from FluidicLib import *
import constants

# Load the fixture configuration
loadpath = "./final_fixture_description.json"
fluidicLib = FluidicLib(loadpath)
strands = fluidicLib.strands

print("=== SCANNING FOR ROGUE LEDs ===")

# Step 1: Scan all LEDs for non-black colors
rogue_leds = []
for i, led in enumerate(fluidicLib.controllers.leds):
    r, g, b = led.color.r, led.color.g, led.color.b
    if (r, g, b) != (0, 0, 0):
        print(f"⚠️  LED {i} is ON → RGB = ({r}, {g}, {b})")
        rogue_leds.append(i)

# Step 2: For each ON LED, try to identify its controlling Pod
print("\n=== CHECKING WHICH POD/FIXTURE OWNS THE ROGUE LEDs ===")
for rogue_index in rogue_leds:
    found = False
    for strand_index, strand in enumerate(strands):
        for pod_index, pod in enumerate(strand):
            if rogue_index in pod.ledIDs:
                print(f"💡 LED {rogue_index} is controlled by strand {strand_index}, pod {pod_index} ({pod})")
                found = True
    if not found:
        print(f"❌ LED {rogue_index} is NOT owned by any Pod!")



print("\n=== RAW BUFFER STATE ===")
fluidicLib.controllers.updateArtnet()  # send current state
fluidicLib.controllers.artnet["1"].printBuffers()  # check buffer for controller 1 (top platform)
fluidicLib.controllers.artnet["3"].printBuffers()  # check buffer for controller 3 (pods)
# OPTIONAL: Uncomment below to force-turn off everything
# print("\n=== FORCING ALL LEDs OFF ===")
# for led in fluidicLib.controllers.leds:
#     led.setColor((0, 0, 0))
# fluidicLib.controllers.updateArtnet()
# print("✅ All LEDs forced to black.")

