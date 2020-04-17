
###################################################################

# This a python code for System response Gm(t) vs t  
# By Moparthi Varun Sankar
# April 17 , 2020 
# Released under GNU GPL

###################################################################
import matplotlib.pyplot as plt
import numpy as np
import math

t = np.linspace(0, 30,1000)

y = (8.00/73.00)*np.cos(2*t) +(152.00/73.00)*np.sin(2*t) + (-8.00/73.00)*np.exp(-3*t/4)

plt.grid()
plt.title("System response gm(t) vs t ")
plt.xlabel("Time")
plt.ylabel("Oscillating system response gm(t)")
plt.plot(t,y)
plt.show()
