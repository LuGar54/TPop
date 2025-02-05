import matplotlib.pyplot as plt
import numpy as np

#efficacité : T = ((2 * w_1 * w_2)/(w_1^2 + w_2^2))*2

Z = []
T = []

for z in range(0, 1000):
    Z.append(z/500)

w_2 = 2203e-9

W0 = 0.315e-3
theta = 0.65e-3
l_ambda = 632.8e-9
f = 0.0045

for z in Z:
    w_objet = W0 * np.sqrt(1 + (z * theta / W0)**2)
    w_1 = l_ambda * f / (np.pi * w_objet)
    
    T.append(((2*w_1*w_2)/(w_1**2 + w_2**2))**2)

z_max = Z[np.argmax(T)]
t_max = max(T)

plt.plot(Z, T)
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=-90")
kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="left", va="top")
plt.annotate(z_max, xy=(z_max, t_max), xytext=(0.20, 0.20), **kw)
plt.grid()
plt.show()