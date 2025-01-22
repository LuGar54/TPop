import matplotlib.pyplot as plt

angles =           [    0,    10,    20,    30,    40,    50,   60,   70,   80,   90,  100,  110,  120,  130,  140,  150,   160,   170,   180]
quartintensity22 = [142.5, 147.9, 147.2, 145.3, 138.0, 117.1, 91.1, 65.8, 46.4, 31.1, 23.3, 22.3, 30.9, 44.0, 63.7, 81.1, 103.4, 125.7, 150.4]
quartintensity45 = [ 87.7,  87.5,  91.2,  98.5,  97.5,  96.3, 92.4, 87.9, 82.4, 82.1, 84.2, 81.6, 79.0, 79.6, 80.2, 80.0,  83.6,  86.8,  92.6]

anglesDemi = [0, 40, 80, 120, 140, 180]
demiIntensity22 = [137.7, 162.4, 64.6, 4.4, 32.0, 136.0]
demiIntensity45 = [17.6, 100.1, 143.2, 92.8, 52.7, 17.2]

plt.plot(angles, quartintensity22, label = "Quart 22")
plt.plot(angles, quartintensity45, label = "Quart 45")

plt.plot(anglesDemi, demiIntensity22, label = "Demi 22")
plt.plot(anglesDemi, demiIntensity45, label = "Demi 45")

plt.legend()
plt.show()