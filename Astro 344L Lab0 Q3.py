import numpy as np
from numpy import sqrt


m = [1.11, .98, .89, 1.031, 1.35, .83]
s = [0.03, .21, .35, .082, .15, .20]
ss = [0.2, 0.2, .2, .2 ,.2 ,.2]

n = len(m)

num = 0
den = 0
num1 = 0
den1 = 0
for i in range(1,n):
    num = num + m[i]/(s[i]**2)
    den = den + (1/s[i]**2)

    num1 = num1 + m[i]/(ss[i]**2)
    den1 = den1 + (1/ss[i]**2)

mean = num/den
mean2 = num1/den1


s1 = 0
s2 = 0
for i in range(1,n):
    s1 = s1 + (m[i] - mean)**2
    s2 = s2 + (m[i] - mean2) ** 2

sd = sqrt((1/(n-1))*s1)
sd2 = sqrt((1/(n-1))*s2)

print(str(round(mean,4)))
print(str(round(sd,4))+'\n')

print(str(round(mean2,4)))
print(str(round(sd2,4)))