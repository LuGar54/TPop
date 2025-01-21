import matplotlib.pyplot as plt

angles = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
te =     []
tm =     []

plt.plot(te, angles, label = "TE")
plt.plot(tm, angles, label = "TM")

plt.legend()
plt.show()