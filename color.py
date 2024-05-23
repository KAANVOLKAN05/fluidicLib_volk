import tween


class Color:
  def __init__(self, r = 0, g = 0, b =0):
    self.set(r, g, b)

  def set(self, r, g, b):
    self.r = r
    self.g = g
    self.b = b

  def black(self):
    self.set(0,0,0)

  def white(self):
    self.set(255,255,255)



# POD_OFF = 0
# POD_FADE_IN = 1
# POD_ON = 2
# POD_FADE_OUT = 3


class FadingColor:
  def __init__(self, color: Color):
    self.targetColor = color
    self.currentColor = Color()
    self.color_tween = {}
    self.__onDuration = 0.0
    self.__fadeOutDuration = 0.0
    self.tweenValue = 0.0

  def get(self):
    return self.currentColor


  def setOff(self):
    # self.bIsTweening = False
    self.currentColor.black()
    self.tweenValue = 0.0
    

  def setOn(self):
    # self.bIsTweening = False
    self.currentColor = self.targetColor
    self.tweenValue = 1.0
    
  def setOnWhite(self):
    self.currentColor.white()

  def update(self):
    # if self.bIsTweening == True:
      self.currentColor.set(self.targetColor.r * self.tweenValue, self.targetColor.g * self.tweenValue, self.targetColor.b * self.tweenValue)
      print ("  " + str(self.tweenValue) + " " + str(vars(self.currentColor)))
      

  def __startFading(self):
    pass
    # self.bIsTweening = True

  def __fadeInEnd(self):
    self.setOn()
    self.__setTween(0.0, self.__fadeOutDuration, self.__onDuration, self.__startFading, self.setOff)

    # self.color_tween = tween.to(self, "tweenValue", 0.0, self.fadeOutDuration, "easeInOutQuad", self.onDuration);
    # self.color_tween.on_update(self.update)
    # self.color_tween.on_start(self.__startFading)
    # self.color_tween.on_complete(self.setOff)

  def __setTween(self, endValue, duration, delay, onStart, onComplete):
    self.color_tween = tween.to(self, "tweenValue", endValue, duration, "easeInOutQuad", delay);
    self.color_tween.on_update(self.update)
    self.color_tween.on_start(onStart)
    self.color_tween.on_complete(onComplete)



  def fadeInOut(self, fadeInDuration:float, onDuration:float, fadeOutDuration:float, startDelay = 0.0):
    # "x", 400, 5.0, "easeInOutQuad"
    # self.tweenStartTime = time.time()

    # self.fadeInDuration = fadeInDuration
    self.__onDuration = onDuration
    self.__fadeOutDuration = fadeOutDuration

    self.__setTween(1.0, fadeInDuration, startDelay, self.__startFading, self.__fadeInEnd)

    # self.state = POD_FADE_IN    

    # self.color_tween = tween.to(self, "tweenValue", 1.0, fadeInDuration, "easeInOutQuad") #Starting a tween.
    # self.color_tween.on_start(self.__startFadeIn) #Adding function that runs at the start of the tween-
    # self.color_tween.on_complete(self.__fadeInEnd)
    # self.color_tween.on_update(self.update)



