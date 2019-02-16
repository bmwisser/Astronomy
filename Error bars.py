import numpy as np
from numpy import sqrt
import math
import matplotlib.pyplot as plt

y = [0.51, 0.73, 0.85, 0.79, 1.14]
dy = [0.07, 0.11, 0.15, 0.18, 0.12]

x = [0.12, 0.18, 0.25, 0.32, 0.38]
dx = [0.02, 0.01, 0.03, 0.02, 0.01]

n = len(y)

plt.xlim([0, 0.5])
plt.ylim([0, 1.3])
plt.xlabel('Time (s)')
plt.ylabel('Length (cm)')
plt.title('Length vs. Time')
plt.grid(True)
plt.errorbar(x, y, fmt='none', xerr=dx, yerr=dy, capsize=5)
plt.scatter(x, y)
plt.show()

