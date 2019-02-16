import numpy as np
import matplotlib.pyplot as plt

#--------------------- Part 1 --------------------------

F12 = [0.88, 0.822, 2.4, 0.273, 2.16, 0.359, 0.345]
F25 = [2.36, 1.31, 2.99, 0.363, 2.18, 1.84, 1.72]
F60 = [32, 21.8, 47.4, 3.6, 32, 11.6, 1.85]
F100 = [128, 215, 215, 44.1, 128, 63.5, 215]

e12_p = [6, 16, 16, 0, 24, 15, 25]; e12 = []
e25_p = [6, 13, 20, 13, 22, 6, 15]; e25 = []
e60_p = [0, 16, 20, 18, 14, 10, 0]; e60 = []
e100_p = [0, 0, 16, 0, 0, 17, 0]; e100 = []

log25o12 = []
e25o12 = []
log60o100 = []
e60o100 = []
for i in range(len(F12)):
    e12.append(e12_p[i] / 100 * F12[i])
    e25.append(e25_p[i] / 100 * F25[i])
    e60.append(e60_p[i] / 100 * F60[i])
    e100.append(e100_p[i] / 100 * F100[i])

    log25o12.append(np.log10(F25[i]/F12[i]))
    e25o12.append(1/np.log(10)*np.sqrt(((e25[i]/F25[i])**2 + (e12[i]/F12[i])**2)))
    
    log60o100.append(np.log10(F60[i]/F100[i]))
    e60o100.append(1/np.log(10)*np.sqrt(((e60[i]/F60[i])**2 + (e100[i]/F100[i])**2)))
    

plt.xlim([-2.5, -0.5])
plt.ylim([-0.2, 1])
plt.xlabel('log(F60/F100)')
plt.ylabel('log(F25/F12)')
plt.title('IRAS Source Colors')
plt.grid(True)
plt.scatter(log60o100, log25o12, color='r')
plt.errorbar(log60o100, log25o12, fmt='none', xerr=e60o100, yerr=e25o12, capsize=5)
plt.show()


#--------------------- Part 2 --------------------------

r = 2300*3.086e16
L_sol = 3.828e26

c = 2.9979e8
wavelength = [12e-6, 25e-6, 60e-6, 100e-6]

flux = [F12[1], F25[1], F60[1], F100[1]]

freq = []
L = []
for i in range(len(flux)):

    freq.append(c/wavelength[i])
    L.append(flux[i]*1e-26*4*np.pi*(r**2)/L_sol)

Lum = np.mean(L)

plt.loglog(freq,flux)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Flux Densitty (Jy)')
plt.title('Flux Density vs Frequency of IRAS 2157+6053')
plt.grid(True)
plt.show()


#--------------------- Part 3 --------------------------

j = [13.853, 14.934, 13.335, 15.782, 12.927, 17.195, 13.706, 15.811, 16.032, 16.449, 14.481, 16.894, 16.273]  # Jmag
je = [0.027, 0.035, 0.022, 0.072, 0.022, 0.215, 0.024, 0.064, 0.073, 0.099, 0.031, 0.143, 0.092]  # Jmag error

h = [13.362, 14.248, 12.872, 15.104, 12.285, 15.816, 12.569, 14.851, 14.658, 15.17, 13.739, 15.964, 15.366]  # Hmag
he = [0.032, 0.049, 0.03, 0.074, 0.028, 0.157, 0.03, 0.071, 0.059, 0.099, 0.036, 0.191, 0.105]  # Hmag error

k = [12.958, 13.865, 12.7, 14.899, 12.071, 15.399, 12.103, 14.366, 14.156, 14.47, 13.446, 15.569, 14.922]  # Kmag
ke = [0.029, 0.046, 0.025, 0.102, 0.02, 0.167, 0.021, 0.063, 0.055, 0.081, 0.038, 0.18, 0.101]  # Kmag error

jh = []; jhe = []
hk = []; hke = []
for i in range(len(j)):

    jh.append(j[i] - h[i])
    jhe.append(np.sqrt(je[i] ** 2 + he[i] ** 2))

    hk.append(h[i] - k[i])
    hke.append(np.sqrt(ke[i] ** 2 + he[i] ** 2))



jk = [-0.21, -0.19, -0.18, -0.17, -0.15, -0.14, -0.13, -0.11, -0.10, -0.08, -0.07, -0.05, -0.04, -0.02, 0.01, 0.02,
      0.04, 0.05, 0.07, 0.09, 0.1, 0.12, 0.14, 0.17, 0.2, 0.24, 0.26, 0.29, 0.31, 0.37, 0.41, 0.47, 0.54, 0.62, 0.67,
      0.72, 0.77, 0.83, 0.86, 0.89, 0.92, 0.90, 0.90, 0.88, 0.89, 0.90, 0.92, 0.95, 0.98, 1.01, 1.05, 1.09, 1.11, 1.14]

HK = [-0.05, -0.05, -0.05, -0.05, -0.04, -0.14, -0.04, -0.03, -0.03, -0.02, 0.02, -0.02, -0.01, -0.01, 0.0, 0.0, 0.01,
      0.01, 0.02, 0.02, 0.02, 0.02, 0.03, 0.04, 0.04, 0.05, 0.06, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.13, 0.14, 0.15,
      0.16, 0.18, 0.19, 0.21, 0.26, 0.28, 0.29, 0.3, 0.31, 0.33, 0.34, 0.36, 0.37, 0.38, 0.40, 0.41, 0.42, 0.43]

JH = []
for i in range(len(jk)):
    JH.append(jk[i] - HK[i])


plt.xlabel('H - K')
plt.ylabel('J - H')
plt.title('Colors of Main Sequence Stars')
plt.grid(True)
plt.plot(HK,JH)
plt.scatter(hk, jh, color='b')
plt.errorbar(hk, jh, color='r', fmt='none', xerr=hke, yerr=jhe, capsize=5)
plt.show()











