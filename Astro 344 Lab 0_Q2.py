import numpy as np
from numpy import sqrt
from math import log, log10

a = 3.14
da = 0.22
b = 2.72
db = 0.16

F1 = sqrt(da**2+db**2)
F2 = sqrt((b*da)**2 + (a*db)**2)
F3 = sqrt((da/b)**2 + (a*db/(b**2))**2)
F4 = (1/log(10))*(da/a)
F5 = (1/log(10))*sqrt((da/a)**2 + (db/b)**2)
F6 = (1/log(10))*sqrt((da/a)**2 + (db/b)**2)

print(round(a-b,2), round(F1,2))
print(round(a*b,2), round(F2,2))
print(round(a/b,2), round(F3,2))
print(round(log10(a),3), round(F4,3))
print(round(log10(a*b),3), round(F5,3))
print(round(log10(a/b),3), round(F6,3))


