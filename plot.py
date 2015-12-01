from __future__ import division
import matplotlib.pyplot as plt
from pdb import set_trace
import pandas as pd
import numpy as np
import time

def plot():
  data  = pd.read_csv('data.csv', header=None) # read a csv file
  last2 = data[data.columns[-2]].values.tolist()
  start = [l for i,l in enumerate(last2) if not i%2]
  end = [l for i,l in enumerate(last2) if i%2]
  delta = [b-a for b,a in zip(end,start)]
  plt.axis([0, 1000, np.mean(delta)-1.96*np.std(delta),np.mean(delta)+1.96*np.std(delta)])
  plt.ion()
  plt.show()
  for i in xrange(49000):
    plt.plot(range(i,i+1000), delta[i:i+1000])
    plt.draw()
    time.sleep(0.05)    # plt.show()
    set_trace()

if __name__=="__main__":
  plot()