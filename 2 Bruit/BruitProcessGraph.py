import matplotlib.pyplot as plt
import numpy as np
import csv
import statistics

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

lowMean = 0
highMean = 0

# for i in range(len(source)):
#     if experience[i] > 1:
#         highMean += source[i]
#     else:
#         lowMean += source[i]
    
# lowMean /= len(source)/2
# highMean /= len(source)/2
lowMean = statistics.mean(lowSource)
highMean = statistics.mean(highSource)

lowArray = np.full_like(time, lowMean)
highArray = np.full_like(time, highMean)

print(lowMean)
print(highMean)
plt.plot(time, lowArray, label = "LowMean")
plt.plot(time, highArray, label = "HighMean")
plt.plot(time, source, label = "Source")
plt.plot(time, experience, label = "On/Off")
plt.legend()
plt.show()
