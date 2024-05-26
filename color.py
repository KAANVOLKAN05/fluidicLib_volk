"""Summary
"""
import tween


class Color:

  """
  Simple class for representing colors
  
  Attributes:
      r (int): Value of the red component of the color. 0 - 255
      g (int): Value of the green component of the color. 0 - 255
      b (int): Value of the blue component of the color. 0 - 255
  """
  
  def __init__(self, r = 0, g = 0, b =0):
    """Constructor for this class
    
    Args:
        r (int, optional): Value of the red component of the color. 0 - 255
        g (int, optional): Value of the green component of the color. 0 - 255
        b (int, optional): Value of the blue component of the color. 0 - 255
    """
    self.set(r, g, b)

  def set(self, r, g, b):
    """set the color values
    
    Args:
        r (int): Value of the red component of the color. 0 - 255
        g (int): Value of the green component of the color. 0 - 255
        b (int): Value of the blue component of the color. 0 - 255
    """
    self.r = r
    self.g = g
    self.b = b


  def black(self):
    """Set the color to black. All values become zero
    """
    self.set(0,0,0)

  def white(self):
    """Set the color to white. All values become 255
    """
    self.set(255,255,255)




class FadingColor:

  
  def __init__(self, color: Color):
    
    self.targetColor = Color(color.r, color.g, color.b)
    self.currentColor = Color()
    self.__color_tween = {}
    self.__onDuration = 0.0
    self.__fadeOutDuration = 0.0
    self.tweenValue = 0.0
    self.__onEndCallback = None

  def get(self):
    return self.currentColor

  def setOff(self):
    self.__setTweenValue(0.0)
    
  def __setTweenValue(self, value):
    self.tweenValue = value
    self.update()

  def setOn(self): 
    
    self.__setTweenValue(1.0)
    
  def setOnWhite(self):
    self.currentColor.white()
    self.tweenValue = 1.0

  def update(self):
    
      self.currentColor.set(self.targetColor.r * self.tweenValue, self.targetColor.g * self.tweenValue, self.targetColor.b * self.tweenValue)
      

  def __fadeOutEnd(self):
    self.__setTweenValue(0.0)
    if callable(self.__onEndCallback):
      self.__onEndCallback()

  def __fadeInEnd(self):
    
    self.__setTweenValue(1.0)
    self.__setTween(0.0 , self.__fadeOutDuration, self.__onDuration, self.__fadeOutEnd)


  def __setTween(self, endValue, duration, delay, onComplete):
    
    self.__color_tween = tween.to(self, "tweenValue", endValue, duration, "easeInOutQuad", delay);
    self.__color_tween.on_update(self.update)
    self.__color_tween.on_complete(onComplete)


  def fadeInOut(self, fadeInDuration:float, onDuration:float, fadeOutDuration:float, startDelay = 0.0, onEndCallback = None):
    """

    
    Args:
        fadeInDuration (float): Description
        onDuration (float): Description
        fadeOutDuration (float): Description
        startDelay (float, optional): Description
        onEndCallback (None, optional): Description
    """
    self.__onEndCallback = onEndCallback
    self.__onDuration = onDuration
    self.__fadeOutDuration = fadeOutDuration


    self.__setTween(1.0, fadeInDuration, startDelay, self.__fadeInEnd)



