import os
import matplotlib.pyplot as plt
import numpy as np

# print(os.getcwd() + '\\DataRaw')

def convert_percent_255(percent):
    percent = max(percent, 0)
    return min(int(np.sqrt(percent) * 255), 255)


def get_percent(sample, specter):
    index = np.argmax(specter)
    adjust_value = 1 - min(0, min(sample))/specter[index]
    # print(min(0, min(sample))/specter[index])
    return (sample[index] * adjust_value - black_specter_y[index])/specter[index]
    

red_specter_y = []
green_specter_y = []
blue_specter_y = []
black_specter_y = []

for filename in os.listdir(os.path.join(os.getcwd(), 'CalibrationData')):
    # print(filename)
    # x = []
    y = []
    with open(os.path.join(os.getcwd(), 'CalibrationData', filename), 'r') as data:
        for line in data.readlines()[13:]:
            p = line.split()
            # x.append(float(p[0]))
            y.append(float(p[1]))

    if 'Red' in filename:
        red_specter_y = y
    elif 'Green' in filename:
        green_specter_y = y
    elif 'Blue' in filename:
        blue_specter_y = y
    elif 'Black' in filename:
        black_specter_y = y
    
for filename in os.listdir(os.path.join(os.getcwd(), 'DataRaw')):
    # print(filename)
    # x = []
    y = []
    with open(os.path.join(os.getcwd(), 'DataRaw', filename), 'r') as data:
        for line in data.readlines()[13:]:
            p = line.split()
            # x.append(float(p[0]))
            y.append(float(p[1]))
    
    percent_red = get_percent(y, red_specter_y)
    r_amount = convert_percent_255(percent_red)
    
    
    percent_green = get_percent(y, green_specter_y)
    g_amount = convert_percent_255(percent_green)
    
    percent_blue = get_percent(y, blue_specter_y)
    b_amount = convert_percent_255(percent_blue)
    print(filename, f'({r_amount}, {g_amount}, {b_amount})')
    