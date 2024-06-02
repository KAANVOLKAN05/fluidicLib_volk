import time, traceback
import threading


class Repeater:
  def __init__(self, delay, task, runThreaded = False):
    self.delay = delay
    self.task = task
    self.next_time = time.time() + delay
    self.running = True
    self.thread = None
    if not runThreaded:
      self.run()
    else:
      self.thread = threading.Thread(target = self.run)
      self.thread.start()

  def stop(self):
    self.running = False
    # if self.thread is not None:
      # self.thread.join()


  def run(self):
    self.next_time = time.time() + self.delay
    while self.running:
      time.sleep(max(0, self.next_time - time.time()))
      try:
        self.task()
      except Exception:
        traceback.print_exc()
        # in production code you might want to have this instead of course:
        # logger.exception("Problem while executing repetitive task.")
      # skip tasks if we are behind schedule:
      self.next_time += (time.time() - self.next_time) // self.delay * self.delay + self.delay




def repeatEvery(delay, task):
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
      task()
    except Exception:
      traceback.print_exc()
      # in production code you might want to have this instead of course:
      # logger.exception("Problem while executing repetitive task.")
    # skip tasks if we are behind schedule:
    next_time += (time.time() - next_time) // delay * delay + delay


def repeatEveryThreaded(delay, task):
  t = threading.Thread(target=lambda: repeatEvery(delay, task))
  t.start()
  return t
  
  



if __name__ == "__main__":

  class TestRepeater:
    def __init__(self):
      self.counter = 0
      self.repeater = None
  
    def run(self):
      self.repeater = Repeater(0.2, self.update, True)
      # print("Repeater ended")
  
  
    def update(self):
      if self.repeater:
        print("Repeater print %d repType: %s"% (self.counter, type(self.repeater)))
        self.counter += 1
        if(self.counter > 10):
          self.repeater.stop()
    
  
  t = TestRepeater()
  
  t.run()
  

# rep.stop()

