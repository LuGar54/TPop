import matplotlib.pyplot as plt

anglesMalus =    [    0,    10,    20,    30,    40,   50,   60,   70,    80,  90, 100,  110,  120,  130,  140,   150,   160,   170,   180]
intensityMalus = [178.6, 177.7, 160.4, 152.5, 123.1, 89.5, 62.5, 37.1,  12.7, 0.9, 4.4, 16.4, 38.8, 66.1, 98.1, 123.1, 154.2, 165.2, 176.1]

plt.plot(anglesMalus, intensityMalus)

plt.show()