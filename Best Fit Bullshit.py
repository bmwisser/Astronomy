import numpy as np
from numpy import sqrt
import matplotlib.pyplot as plt

# y = [0.51, 0.73, 0.85, 0.79, 1.14]
# dy = [0.07, 0.11, 0.15, 0.18, 0.12]
#
# x = [0.12, 0.18, 0.25, 0.32, 0.38]

# y = [2.64915576546339, 2.42304463067876, 2.18965811624781, 1.95305131098099, 1.71639756752593, 1.482757

y = [2.59959456184083, 2.35629846300746, 2.11338798642443, 1.87328066729511, 1.63133096193888, 1.38375602309728, 1.13627937095618,
     0.890246608317685, 0.641657231379256, 0.388663709251197, 0.162391020499244,]

dy = [0.0031626080937992, 0.00381663020646705, 0.00520710108772981, 0.00899932564258888, 0.0442504790296486, 0.0144038850081185,
      0.00637752377912799, 0.00428219550595217, 0.0033769473746838, 0.00293351356230806, 0.00275613036877875]

x = [0,1,2,3,4,5,6,7,8,9,10]

# x = [57995.7991039999, 57996.7741029998, 57997.7741, 57998.7824329999, 57999.7824320001, 58000.7824309999, 58001.774096,
#      58002.7824269998, 58003.7824260001, 58004.7824249998, 58005.7824249998]

n = len(y)

sx = 0
sx2 = 0
sy = 0
sxy = 0

xod = 0
x2od = 0
yod = 0
xyod = 0
od2 = 0
for i in range(0, n):
    sx = sx + x[i]
    sx2 = sx2 + (x[i]**2)
    sy = sy + y[i]
    sxy = sxy + x[i]*y[i]

    xod = xod + (x[i]/(dy[i]**2))
    x2od = x2od + (x[i]**2)/(dy[i]**2)
    yod = yod + (y[i]/(dy[i]**2))
    xyod = xyod + (x[i]*y[i])/(dy[i]**2)
    od2 = od2 + (1/(dy[i]**2))

a = (n*sxy - sx*sy)/(n*sx2 - (sx**2))
b = (sx2*sy - sx*sxy)/(n*sx2 - (sx**2))

s = 0
for i in range(0, n):
    s = s + (y[i] - a*x[i] - b)**2

S = sqrt(s/(n-2))

da = S * sqrt(n/(n*sx2 - (sx**2)))
db = S * sqrt(sx2/(n*sx2 - (sx**2)))

print(str(round(a,4))+' \u00B1 '+str(round(da,4)))
print(str(round(b,4))+' \u00B1 '+str(round(db,4))+'\n')

a1 = (xod*yod - xyod*od2)/((xod**2) - x2od*od2)
b1 = (xod*xyod - yod*x2od)/((xod**2) - x2od*od2)

da1 = sqrt(od2/(x2od*od2 - (xod**2)))
db1 = sqrt(x2od/(x2od*od2 - (xod**2)))

print(str(round(a1,4))+' \u00B1 '+str(round(da1,4)))
print(str(round(b1,4))+' \u00B1 '+str(round(db1,4)))

dx = np.linspace(0,10,30)

plt.close('all')
plt.errorbar(x, y, yerr=dy, fmt='none', capsize=5)
plt.scatter(x, y , marker='o', color='b')
# plt.xlim([0,0.5])
# plt.ylim([0,1.3])
plt.axis('auto')
plt.xlabel('X (s)')
plt.ylabel('Y (cm)')
plt.grid(True)
plt.title('Y vs. X')

plt.plot(dx, a*dx + b, 'c', label='Excluding uncertainty')
plt.plot(dx, a1*dx + b1, '--r', label='Including uncertainty')
plt.legend()
plt.show()




