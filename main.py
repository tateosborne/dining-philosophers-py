import threading

class Philosopher(threading.Thread):
  
  def __init__(self, idx, forkL, forkR, eaten) -> None:
    threading.Thread.__init__(self)
    self.idx = idx
    self.forkL = forkL
    self.forkR = forkR
    self.eaten = eaten
      
      
  def dinner_time(self):
    if self.eaten:
      return
    else:
      while self.forkL and self.forkR == True:
        self.
        
def main():
  forks = [threading.Semaphore() for n in range(8)]
  philosophers = [Philosopher(i, forks[i % 8], forks[i+1 % 8], False) for i in range(8)]
  
  Philosopher.running = True
  for p in philosophers[p]:
    p.dinner_time()
 
 
if __name__ == "__main__":
  main()
  