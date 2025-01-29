import matplotlib.pyplot as plt

anglesMalus =    [    0,    10,    20,    30,    40,   50,   60,   70,    80,  90, 100,  110,  120,  130,  140,   150,   160,   170,   180]
intensityMalus = [178.6, 177.7, 160.4, 152.5, 123.1, 89.5, 62.5, 37.1,  12.7, 0.9, 4.4, 16.4, 38.8, 66.1, 98.1, 123.1, 154.2, 165.2, 176.1]

angles =           [    0,    10,    20,    30,    40,    50,   60,   70,   80,   90,  100,  110,  120,  130,  140,  150,   160,   170,   180]
quartintensity22 = [142.5, 147.9, 147.2, 145.3, 138.0, 117.1, 91.1, 65.8, 46.4, 31.1, 23.3, 22.3, 30.9, 44.0, 63.7, 81.1, 103.4, 125.7, 150.4]
quartintensity45 = [ 87.7,  87.5,  91.2,  98.5,  97.5,  96.3, 92.4, 87.9, 82.4, 82.1, 84.2, 81.6, 79.0, 79.6, 80.2, 80.0,  83.6,  86.8,  92.6]

anglesDemi = [0, 40, 80, 120, 140, 180]
demiIntensity22 = [137.7, 162.4, 64.6, 4.4, 32.0, 136.0]
demiIntensity45 = [17.6, 100.1, 143.2, 92.8, 52.7, 17.2]

anglespol = [  10,   15,   20,   25,   30,   35,   40,   45,   50,   55,   60,   65,    70,    75,    80]
te =     [16.4, 17.4, 18.9, 21.2, 24.0, 27.6, 32.2, 38.2, 47.7, 59.4, 75.7, 92.9, 125.8, 174.0,   240]
tm =     [15.7, 15.0, 13.9, 11.8, 10.2,  8.5,  6.4,  4.3,  2.2,  1.2,  1.9,  6.2,  20.5,  50.7, 108.7]


plt.subplot(2, 2, 1)
plt.plot(anglespol, te, label = "TE")
plt.plot(anglespol, tm, label = "TM")
plt.legend()
plt.title("Polarisation TE et TM")


plt.subplot(2, 2, 2)
plt.plot(angles, quartintensity22, label = "Quart 22")
plt.plot(angles, quartintensity45, label = "Quart 45")
plt.legend()
plt.title("Lames à retard de phase d'un quart de longueur d'onde")


plt.subplot(2, 2, 3)
plt.plot(anglesDemi, demiIntensity22, label = "Demi 22")
plt.plot(anglesDemi, demiIntensity45, label = "Demi 45")
plt.legend()
plt.title("Lames à retard de phase d'une demi longueur d'onde")


plt.subplot(2, 2, 4)
plt.plot(anglesMalus, intensityMalus, label = "Malus")

plt.title("Loi de Malus")
plt.show()