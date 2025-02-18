import pandas
import matplotlib.pyplot as plt


csvDots = pandas.read_csv('SimpleFenteInstagramReels.csv', usecols=['Gray_Value'])
csv2F4D = pandas.read_csv('DoubleFenteInstagramReels.csv', usecols=['Gray_Value'])
#X =range(len(csv2F4D))
#print(X)

plt.plot(csvDots)
plt.plot(csv2F4D)
plt.show()