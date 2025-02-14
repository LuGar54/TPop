import pandas
import matplotlib.pyplot as plt


csvDots = pandas.read_csv('DiffractionDots.csv', usecols=['Gray_Value'])

plt.plot(csvDots)
plt.show()