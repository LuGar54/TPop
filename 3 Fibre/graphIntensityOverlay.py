import matplotlib.pyplot as plt
import pandas


img = plt.imread("patternCrop.jpg")

csvFile = pandas.read_csv('Multimode_haut.csv', usecols=['Gray_Value'])

plt.imshow(img, origin='lower', extent=[0, len(csvFile), 0, 100], aspect='auto')


plt.plot(csvFile)

plt.show()
