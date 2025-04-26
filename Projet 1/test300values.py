import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# plt.bar([0, 20, 40, 60, 80, 100], [0, 0.2, 0.4, 0.6, 0.8, 1], width=5)
# plt.xlabel("Pourcentage d'éthanol (%)", fontsize=15)
# plt.ylabel('Intensité (relative)', fontsize=15)
# plt.savefig("bar.png")
# plt.show()

def open_file(file_to_compare):
    x = []
    y = []
    all_y = []
    folder = './Data2CM/'
    if '11_03' in file_to_compare:
        folder = './DataRamanCM/'
        
    with open(folder + file_to_compare, 'r') as data:
        for line in data:
            p = line.split()
            all_y.append(float(p[1]))
            currentPixel = float(p[0])
            if currentPixel < 2000 and currentPixel > 800:
                x.append(float(p[0]))
                y.append(float(p[1]))
    # print(max(all_y))
    return x, y


files_to_compare = [
    ('15_04_ethanol_100_300sec_1.txt', 100),
    ('15_04_ethanol_80_300sec_1.txt', 80),
    ('15_04_ethanol_60_300sec_1.txt', 60),
    ('15_04_ethanol_40_300sec_1.txt', 40),
    ('15_04_ethanol_20_300sec_1.txt', 20),
    # ('11_03_ethanol_100_Reference_100sec_aligned_1.txt', 100),
    # ('11_03_ethanol_80_Reference_100sec_1.txt', 80),
    # ('11_03_ethanol_60_Reference_100sec_1.txt', 60),
    # ('11_03_ethanol_40_Reference_100sec_1.txt', 40),
    # ('11_03_ethanol_20_Reference_100sec_1.txt', 20),
    # ('11_03_ethanol_0_Reference_100sec_1.txt', 0),
    ('11_03_gin_Reference_100sec_1.txt', 30),
    ('11_03_vodka_Reference_100sec_1.txt', 30),
    ('11_03_whisky_Reference_100sec_1.txt', 30)
]

heights = []
concentrations = []

substrats = []

for file_to_compare, concentration in files_to_compare:
    x, y = open_file(file_to_compare)  

    ground = np.mean(y[50:120])

    if 'whisky' in file_to_compare:
        ground = np.mean(y[50:100] + y[150:300])
    
    pos_max = np.argmax(y[120:300]) + 120
    # print(pos_max)
    
    peak_height = (y[pos_max] - ground)* (concentration**0.6)
    print(file_to_compare, np.std(y[50:90])/peak_height * 100)
    
    if 'et' in file_to_compare:
        heights.append(peak_height)
        concentrations.append(concentration)
    else:
        substrats.append((peak_height-2050, file_to_compare))
        
    # plt.scatter(x[pos_max], y[pos_max], color='red', label='Max Peak')
    # plt.vlines(x[pos_max], ground, y[pos_max], color='green', linestyle='--', label='Peak Height')

    # plt.scatter(x[90], y[90], color='blue', label='Data Points')

    plt.xlabel("Longueur d'onde (cm-1)", fontsize=15)
    plt.ylabel('Intensité (relative)', fontsize=15)
    plt.plot(x, y)
    plt.show()
    
    
def test_linear_fitting(x, a, b):
    return a * x + b

def invert_fit(y, a, b):
    return (y - b) / a

maxHeight = max(heights)

heights = heights/maxHeight

param, param_cov = curve_fit(test_linear_fitting, concentrations, heights)

fits = []

print(param_cov)

for i in concentrations:
    fits.append(test_linear_fitting(i, param[0], param[1]))
    
top_diff = max(np.subtract(heights,fits))
bottom_diff = min(map(lambda h, f: h - f, heights, fits))

for substrat, file_name in substrats:
    # plt.hlines(substrat/maxHeight, 0, 100, color='black', linestyle='--', label='Substrat Peak Height')
    center = invert_fit(substrat/maxHeight, param[0], param[1])
    top = invert_fit(substrat/maxHeight, param[0], param[1]+top_diff)
    bottom = invert_fit(substrat/maxHeight, param[0], param[1]+bottom_diff)
    print(file_name, bottom, center, top)
    color = 'magenta'
    legend = 'Vodka'
    if 'gin' in file_name:
        color = 'blue'
        legend = 'Gin'
    elif 'whisky' in file_name:
        color = 'green'
        legend = 'Whisky'
        
    plt.hlines(substrat/maxHeight, bottom, top, color=color, linestyle='--', label=legend)

plt.plot(concentrations, fits + top_diff, color='black', linestyle='dashed', label='_nolegend_')
plt.plot(concentrations, fits, color=(0.12, 0.47, 0.7, 0.5), label='_nolegend_')
plt.plot(concentrations, fits + bottom_diff, color='black', linestyle='dashed', label='_nolegend_')
plt.xlim(34, 50)
plt.ylim(0.22, 0.32)
# plt.scatter(concentrations, heights)
plt.legend()
plt.xlabel("Pourcentage d'éthanol (%)", fontsize=15)
plt.ylabel('Intensité (relative)', fontsize=15)
plt.title("Intensité du spectre Raman selon le taux d'éthanol", fontsize=15)
plt.gca().invert_xaxis()
plt.savefig("results.png")
plt.show()