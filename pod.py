
from color import *



BLINK_DEFAULT_DURATION = 4.0


class Pod:
  def __init__(self, name:str, color: Color, type:int, index:int, universe:int, controllerId:int):
    self.type = type
    self.name = name
    self.index = index
    self.universe = universe
    self.controllerId = controllerId
    self.color = FadingColor(color)
    

    # self.tweenStartTime = 0.0
    # self.state = POD_OFF
    # self.color_tween = {}
    

    # self.fadeInDuration = BLINK_DEFAULT_DURATION
    # self.onDuration = BLINK_DEFAULT_DURATION
    # self.fadeOutDuration = BLINK_DEFAULT_DURATION
    

  def setOff(self):
    self.color.setOff()
    # self.state = POD_OFF
    # self.currentColor.black()
    # self.tweenValue = 0.0
    

  def setOn(self):
    self.color.setOn()
    # self.state = POD_ON
    # self.currentColor = self.color
    # self.tweenValue = 1.0
    

  # def setOnWhite(self):
  #   self.state = POD_ON
  #   self.currentColor.white()

  # def __setFadeIn(self):
  #   self.state = POD_FADE_IN

  # def __setFadeOut(self):
  #   self.state = POD_FADE_OUT

  # def update(self):
    # if self.state == POD_OFF or self.state == POD_ON:
    #   return
    # else:
    #   self.currentColor.set(self.color.r * self.tweenValue, self.color.g * self.tweenValue, self.color.b * self.tweenValue)
    #   print (self.name + " __updateTweenIn() " + str(self.tweenValue) + " " + str(vars(self.currentColor)))
      
  
  # def __fadeInEnd(self):

  #   self.color_tween = tween.to(self, "tweenValue", 0.0, self.fadeOutDuration, "easeInOutQuad", self.onDuration);
  #   self.color_tween.on_update(self.update)
  #   self.color_tween.on_start(self.__setFadeOut)
  #   self.color_tween.on_complete(self.setOff)


  def blink(self, fadeInDuration:float = BLINK_DEFAULT_DURATION, onDuration:float = BLINK_DEFAULT_DURATION, fadeOutDuration:float = BLINK_DEFAULT_DURATION, startDelay = 0.0):
    self.color.fadeInOut(fadeInDuration, onDuration, fadeOutDuration, startDelay)
    # "x", 400, 5.0, "easeInOutQuad"
    # self.tweenStartTime = time.time()

    # self.fadeInDuration = fadeInDuration
    # self.onDuration = onDuration
    # self.fadeOutDuration = fadeOutDuration

    # self.state = POD_FADE_IN    

    # self.color_tween = tween.to(self, "tweenValue", 1.0, fadeInDuration, "easeInOutQuad") #Starting a tween.
    # self.color_tween.on_start(self.__setFadeIn) #Adding function that runs at the start of the tween-
    # self.color_tween.on_complete(self.__fadeInEnd)
    # self.color_tween.on_update(self.update)

