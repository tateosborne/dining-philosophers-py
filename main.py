from pickle import TRUE
import threading

class Philosopher(threading.Thread):
  # boolean field which is flagged true until all Philosophers have eaten
  complete = False
  
  def __init__(self, idx, forkL, forkR, eaten) -> None:
    self.idx = idx
    self.forkL = forkL
    self.forkR = forkR
    threading.Thread.__init__(self)
    
  def begin(self):
    while not self.complete:
      self.dinner_time()
      
  def dinner_time(self):
    forkleft = self.forkL
    forkright = self.forkR
    while not self.complete:
      pass
        
def main():
  philosophers = []
  forks = []
  for i in range(5):
    forks[i] = threading.Semaphore
  for i in range(5):
    philosophers[i] = Philosopher(i, forks[i%5], forks[(i+1)%5])
  
  for phil in philosophers:
    phil.begin()
 
if __name__ == "__main__":
  main()