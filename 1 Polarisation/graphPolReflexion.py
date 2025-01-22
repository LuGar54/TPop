import matplotlib.pyplot as plt

angles = [  10,   15,   20,   25,   30,   35,   40,   45,   50,   55,   60,   65,    70,    75,    80]
te =     [16.4, 17.4, 18.9, 21.2, 24.0, 27.6, 32.2, 38.2, 47.7, 59.4, 75.7, 92.9, 125.8, 174.0,   240]
tm =     [15.7, 15.0, 13.9, 11.8, 10.2,  8.5,  6.4,  4.3,  2.2,  1.2,  1.9,  6.2,  20.5,  50.7, 108.7]

plt.plot(angles, te, label = "TE")
plt.plot(angles, tm, label = "TM")

plt.legend()
plt.show()