import matplotlib.pyplot as plt
import numpy as np
import csv

time = []
source = []
highSource = []
lowSource = []
experience = []

with open('./BruitOnSansFiltreCommence0_20250129_094727_Traces.csv', mode='r') as file:
    csvFile = csv.reader(file)
    firstLine = False
    for lines in csvFile:
        # print(lines)
        if not firstLine:
            firstLine = True
            continue
        time.append(float(lines[0]))
        src = float(lines[1])
        source.append(src)
        exp = float(lines[2])
        experience.append(exp)
        if exp > 1:
            highSource.append(src)
        else:
            lowSource.append(src)

lowMean = np.mean(lowSource)
highMean = np.mean(highSource)
print(lowMean)
print(highMean)
# number of sample
num = [2, 10, 50, 200]
# list of sample means
means = []  

for j in num:
    x = []
    for a in range(1000):
        total = 0
        for i in range(j):
            total += highSource[np.random.randint(0, len(highSource))]
        # print(total/j)
        x.append(total/j)
        
    means.append(x)
k = 0

# plotting all the means in one figure
fig, ax = plt.subplots(2, 2, figsize =(8, 8))
for i in range(0, 2):
    for j in range(0, 2):
        # Histogram for each x stored in means
        ax[i, j].hist(means[k], 30, density = True)
        ax[i, j].set_title(label = num[k])
        if (i == 1):
            ax[i, j].set_xlabel("Valeur des moyennes")
            
        if (j == 0):
            ax[i, j].set_ylabel("Nombre de moyennes")
            
        k = k + 1

plt.show()