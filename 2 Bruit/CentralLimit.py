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

print(np.std(source)/np.sqrt(len(source)))
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

# print(np.mean(means[0])-min(means[0]))
# print(-np.mean(means[0])+max(means[0]))

bins = np.histogram(np.hstack((means[0], means[3])), bins=50)[1]
plt.subplot(2, 1, 1)
plt.hist(means[3], bins, alpha=0.25, label=f"{num[3]}", edgecolor='black', hatch='/')
plt.hist(means[2], bins, alpha=0.25, label=f"{num[2]}", edgecolor='black', hatch='++')
plt.hist(means[1], bins, alpha=0.25, label=f"{num[1]}", edgecolor='black', hatch='\\')
plt.hist(means[0], bins, alpha=0.25, label=f"{num[0]}", edgecolor='black', hatch='xxx')
plt.legend()

plt.xlabel("Moyenne du signal [V]")
plt.ylabel("Nombre d'échantillon ayant cette moyenne")

plt.subplot(2, 1, 2)

stds = []
for i in range(len(means)):
    stds.append(np.std(means[i]))

plt.xlabel("Nombre d'échantillons")
plt.ylabel("Écart type [V]")

plt.plot(num, stds)
# plotting all the means in one figure
# fig, ax = plt.subplots(2, 2, figsize =(8, 8))
# for i in range(0, 2):
#     for j in range(0, 2):
#         # Histogram for each x stored in means
#         ax[i, j].hist(means[k], 30, density = True)
#         ax[i, j].set_title(label = num[k])
#         if (i == 1):
#             ax[i, j].set_xlabel("Valeur des moyennes")
            
#         if (j == 0):
#             ax[i, j].set_ylabel("Nombre de moyennes")
            
#         k = k + 1

plt.show()