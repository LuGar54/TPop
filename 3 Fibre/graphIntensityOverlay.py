import matplotlib.pyplot as plt
import numpy as np
import pandas
from PIL import Image
import matplotlib.patheffects as pe


#img = plt.imread("Monomode.jpg", )

im =np.array(Image.open('Leger monomode.jpg').convert('L'))
csvFileHM = pandas.read_csv('Multimode_haut.csv', usecols=['Gray_Value'])
csvFileLM = pandas.read_csv('Leger multimode.csv', usecols=['Gray_Value'])
csvFileM = pandas.read_csv('monomode.csv', usecols=['Gray_Value'])


plt.style.use('grayscale')
plt.imshow(im, origin='lower' ,extent=[0, len(csvFileLM), 0, 100], aspect='auto')


plt.plot(csvFileLM,path_effects=[pe.Stroke(linewidth=5, foreground='w'), pe.Normal()])
plt.title("Légèrement multimode")
plt.xlabel('Position des pixels')
plt.ylabel('Intensité [%]')
plt.show()
