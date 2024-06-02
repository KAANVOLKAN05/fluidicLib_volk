# fuidicLib


Python Library for controlling [Fluidic Data](https://agneschavez.com/portfolio/fluidic-data/)'s lights


## Purpose

* Control lights through Artnet protocol
* Abstract out the handling of Artnet so it is not necesary to deal with any of it while sequencing the lights
* Allow for custom sequences of lights, which would show the decay's of particles, in a flexible and simple way.
* Simple interface, yet powerful allowing for custom sequences with several variations.


## Install

First you will need to run the following in order to install the required external libraries

* Open a terminal sesion
* `cd` into the folder of this library.
* Run the following command:
`pip3 install -r requirements.txt`

## Usage
Check the `example.py` file for real code that you should be able to run.
The explanation to that code is what follows

### Initing
First you need to import this library

```python
from FluidicLib import *
```

Then initialize it

```python
fluidicLib = FluidicLib("./final_fixture_description.json")
```

This initialization process will load the json file from the passed file path and it will do the following: 

* Create Pod objects, each representing a pod with its corresponding artnet addresses and other specifications of it. Each pod object has only a single predefined color, even when in reality each Pod might have one or two LED lights, each with several different addressable lights, yet this abstraction allows to set properly the all the Artnet values to have the correct value with out having to care about channels or universes or actually any Artnet at all.
* each column of the instalation or strand are stored on an array, where each strand contains, also in an array each pod thus having a "2D array". 
* Create Artnet controller objects, one for each real controller and internally control the necesary universes for each. These are created from the specs passed in the json file.
* Creating a mapping from the Pod objects to the artnet controllers so these can be updated automatically upon changing the color of any pod.
* Initialize the sequencing engine. 

Once all this is done you can put your code for the sequences. 

By default, just loading the library will not change anything in the lights.

### Accessing pod objects

Each Pod object is associated with a a strand (experiment) and a particle and are stored in `fluidicLib.strands[Strand Index][Particle Index]`.

To make code cleaner and shorter just make an alias to the strand's array
`strands = fluidicLib.strands`

You can either access this indices with numbers or use the explicit constants which will make it easier to identify and work with this. 
Such as `strands[ATLAS][ELECTRON]`

These constants are in the [constants.py](constants.py) file


You can turn on or off each pod by calling on them either `setOn()` or `setOff()`, for example `strands[ATLAS][ELECTRON].setOn()`

You mostly want to access the pod objects in order to create sequences of animations, described below


### Sequencing

The sequencing of the pods is done using Chain objects. A Chain is made of a collection of ChainLinks. Each ChainLink represents a light animation for a single pod.
Once an animation ends it triggers the next in the chain. A Chain can branch so it triggers 2 pod animations at the same time

### Animation parameters
This animations could be blink once, blink a certain amount of times, blink infinitely, turn on or turn off. For any of these you can define the timings of the blink. There are 4 values for this timings:

* Fade in duration 
* On duration
* Fade out duration
* Fade in delay (off duration)

#### Defaults
The default animation parameters are stored in 

```python
BLINK_DEFAULT_ON_DURATION
BLINK_DEFAULT_FADE_IN_DURATION
BLINK_DEFAULT_FADE_OUT_DURATION
BLINK_DEFAULT_START_DELAY
```

All these values are floating point numbers expressing seconds.

You can either pass values for each off these when creating a ChainLink or not which will use the defaults.

#### Simplest animation
The simplest animation would be to just make a ChainLink and reapeat forever with the default blinking timings

```python
chainLink = ChainLink(strands[ATLAS][ELECTRON])
# chainLink = ChainLink(strands[ATLAS][ELECTRON], 1.0, 3.0, 2.0, 0.5) # with non default blink timings
chainLink.repeatInfinite()
chainLink.start()
```

As you would expect this will make the Electron Pod of the Atlas strand to blink forever.

Blinking does not start until you call the start function of the chainLink. This allows you to create multiple animations and trigger these depending you your needs. Try not to start multiple animations for the same pod at the same time as this will create an undefined behavior


### Chains

The Chain object takes in either a list which will create a sequential animation or  a tuple that will create a branching animation. 
Lists are made with square brackets [], tuples with parenthesis ()

In a sequential animation once one animation ends it will start the following one. It can be any number of elements, even repeated elements

A branching animation, takes in a tuple with exactly 3 elements. Once the first animation ends it will trigger the following 2.

```python
# make a referece to keep code cleaner and shorter
atlas = strands[ATLAS]

sequentialChain = Chain([atlas[ELECTRON], atlas[MUON], atlas[TAU]]

branchingChain = Chain((atlas[QUARK_DOWN], atlas[QUARK_UP], atlas[QUARK_STRANGE])) 

# calling branchingChain.start() will start the animation for atlas[QUARK_DOWN] and when it ends it will start at the same time atlas[QUARK_UP] and atlas[QUARK_STRANGE]

```

### Nesting

Chains are nestable, meaning that you can create complex animations by putting one animation inside another one

```python
seqChain = Chain([atlas[ELECTRON], atlas[MUON], atlas[TAU]])
branch0 = (atlas[QUARK_UP], atlas[QUARK_DOWN], atlas[PHOTON])
branch1 = [atlas[W_BOSON], atlas[ELECTRON_NEUTRINO], atlas[MUON_NEUTRINO]]

chain = Chain([seqChain, (atlas[QUARK_DOWN], branch0, branch1)])

```

you can create the same by calling it all in a single line, 

```python
chain = Chain([[atlas[ELECTRON], atlas[MUON], atlas[TAU]], (atlas[QUARK_DOWN], (atlas[QUARK_UP], atlas[QUARK_DOWN], atlas[PHOTON]), (atlas[W_BOSON], atlas[ELECTRON_NEUTRINO], atlas[MUON_NEUTRINO]))])
```

### Checking structure
you can call on printStructure() on any Chain  and it will print its nested structure.

```python
chain = Chain([[atlas[ELECTRON], atlas[MUON], atlas[TAU]], (atlas[QUARK_DOWN], (atlas[QUARK_UP], atlas[QUARK_DOWN], atlas[PHOTON]), (atlas[W_BOSON], atlas[ELECTRON_NEUTRINO], atlas[MUON_NEUTRINO]))])

chain.printStructure()

```

## Local development

In order to make development easier and make sure you will get what you intend to you can use 
`loadpath = "./final_fixture_description_localhost.json"` as the path you use to initialize FluidicLib.

This will send all artnet messages to localhost so you can check on an Artnet receiver app.
### macos 
Try using the macos app included in `local_dev/macos/FluidicDataArtNetReceiver.zip`. Unzippit. 
The first time you run it you might need to do the following:

1. Once you've uncompressed the downloaded app, you need to move it elsewhere. This is a think that apple has called translocation, I guess it is for security reasons.
Just drag it into the desktop (if you had it not in the desktop).
2. open the terminal, paste the following:

`xattr -dr com.apple.quarantine`

make sure there is a space after quarantine. drag and drop the app into the terminal window and press enter.


3. close the terminal and now open the app by double clicking.

Just keep this app running. and it will display whenever the python script sends anything.



















