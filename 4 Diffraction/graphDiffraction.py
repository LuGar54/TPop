import pandas
import matplotlib.pyplot as plt
import numpy as np


csv1F = np.array(pandas.read_csv('TEST.csv', usecols=['Gray_Value'])['Gray_Value'].tolist())
csv2F4D = np.array(pandas.read_csv('DoubleFenteInstagramReels.csv', usecols=['Gray_Value'])['Gray_Value'].tolist())-50

maxi = max(csv2F4D)

print(maxi)

x1 = np.linspace(-1, 1, num=len(csv1F))
x2 = np.linspace(-1, 1, num=len(csv2F4D))
plt.title("Comparaison fente simple et double")
plt.xlabel("Position arbitraire")
plt.ylabel("Intensité lumineuse (%)")
plt.plot(x1, np.array(csv1F)/maxi * 100, color="darkgray")
plt.plot(x2, np.array(csv2F4D)/maxi * 100, "--", color="black")
plt.savefig("fenteSimple-Double.pdf")
plt.show()