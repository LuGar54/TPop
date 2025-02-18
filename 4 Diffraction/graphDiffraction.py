import pandas
import matplotlib.pyplot as plt


csv1F = pandas.read_csv('TEST.csv', usecols=['Gray_Value'])
csv2F4D = pandas.read_csv('DoubleFenteInstagramReels.csv', usecols=['Gray_Value'])


#X =range(len(csv2F4D))
#print(X)

plt.plot(csv1F)
plt.plot(csv2F4D-50)
plt.show()