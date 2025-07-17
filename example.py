from FluidicLib import *


loadpath = "./final_fixture_description_localhost.json"

fluidicLib = FluidicLib(loadpath)




atlas = fluidicLib.strands[ATLAS]



# chainLink = ChainLink(atlas[ELECTRON])
# # chainLink = ChainLink(atlas[ELECTRON], 1.0, 3.0, 2.0, 0.5) # with non default blink timings
# chainLink.repeatInfinite()
# chainLink.start()


chain = Chain(([atlas[ELECTRON], atlas[MUON], atlas[TAU]], (atlas[QUARK_DOWN], (atlas[QUARK_UP], atlas[QUARK_DOWN], atlas[PHOTON]), (atlas[W_BOSON], atlas[ELECTRON_NEUTRINO], atlas[MUON_NEUTRINO])), atlas[TAU_NEUTRINO]))


# chain = Chain([[atlas[ELECTRON], atlas[MUON], atlas[TAU]], (atlas[QUARK_DOWN], (atlas[QUARK_UP], atlas[QUARK_DOWN], atlas[PHOTON]), (atlas[W_BOSON], atlas[ELECTRON_NEUTRINO], atlas[MUON_NEUTRINO]))])

# chain = Chain((atlas[QUARK_DOWN], (atlas[QUARK_UP], atlas[QUARK_DOWN], atlas[PHOTON]), (atlas[W_BOSON], atlas[ELECTRON_NEUTRINO], atlas[MUON_NEUTRINO])))

# seqChain = Chain([atlas[ELECTRON], atlas[MUON], atlas[TAU]])
# branch0 = Chain((atlas[QUARK_UP], atlas[QUARK_DOWN], atlas[PHOTON]))
# branch1 = Chain([atlas[W_BOSON], atlas[ELECTRON_NEUTRINO], atlas[MUON_NEUTRINO]])

# chain = Chain([seqChain, (atlas[QUARK_DOWN], branch0, branch1)])
# 1) spin up the updater
updater = Repeater(1.0/30,
    lambda: tween.update(1.0/30),  # always pass a constant dt
    runThreaded=True
)

# 2) register chain‐finished → updater.stop()
chain._onFinished = updater.stop   # or subclass Chain as shown earlier

chain.printStructure()

# chain.repeatInfinite()
chain.repeatTimes(1)
chain.start() 






