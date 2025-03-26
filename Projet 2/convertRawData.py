import os
import matplotlib.pyplot as plt

# print(os.getcwd() + '\\DataRaw')

for filename in os.listdir(os.path.join(os.getcwd(), 'DataRaw')):
    # print(filename)
    x = []
    y = []
    with open(os.path.join(os.getcwd(), 'DataRaw', filename), 'r') as data:
        for line in data.readlines()[13:]:
            p = line.split()
            x.append(float(p[0]))
            y.append(float(p[1]))

    with open(os.path.join(os.getcwd(), 'ConvertedData', filename), 'w') as data:
        
