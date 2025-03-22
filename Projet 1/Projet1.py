import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks, savgol_filter
from scipy.optimize import curve_fit
from matplotlib.patches import Polygon
from sklearn.preprocessing import normalize
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


MAX_PLATEAU = 8
DIFF_BETWEEN_PLATEAUS = 150

def open_file(file_to_compare):
    x = []
    y = []
    with open('./DataRamanCM/' + file_to_compare, 'r') as data:
        for line in data:
            p = line.split()
            currentPixel = float(p[0])
            if currentPixel < 2000 and currentPixel > 800:
                x.append(float(p[0]))
                y.append(float(p[1]))
    return x, y

def find_plateau(points, peak_index, peak_y):
    plateaued_times = 0
    last = peak_y
    index = 0
    for i in points[peak_index:]:
        if abs(i - last) < DIFF_BETWEEN_PLATEAUS:
            plateaued_times += 1
            # print(plateaued_times)
            if plateaued_times >= MAX_PLATEAU:
                return max(0, peak_index - index - MAX_PLATEAU)
    
        else:
            plateaued_times = 0
        last = i
        index += 1
    return 0

x_ref, y_ref = open_file('11_03_ethanol_100_Reference_100sec_aligned_1.txt')

files_to_compare = [
    ('11_03_ethanol_100_Reference_100sec_aligned_1.txt', 5110),
    ('11_03_ethanol_80_Reference_100sec_1.txt', 5007),
    ('11_03_ethanol_60_Reference_100sec_1.txt', 4099),
    ('11_03_ethanol_40_Reference_100sec_1.txt', 2955),
    ('11_03_ethanol_20_Reference_100sec_1.txt', 1532),
    ('11_03_ethanol_0_Reference_100sec_1.txt', 0),
    ('11_03_gin_Reference_100sec_1.txt', 3093),
    ('11_03_vodka_Reference_100sec_1.txt', 3040),
    ('11_03_whisky_Reference_100sec_1.txt', 2988)
]

prominences = []
alcools = []

prominences_down_noise = []
alcools_down_noise = []

prominences_up_noise = []
alcools_up_noise = []

for file_to_compare, peak_height in files_to_compare:
    
    x, y = open_file(file_to_compare)  
    
    # print(x[518])

    # print(old_max)
    normalized_y = normalize([y], norm='max')
    # plt.plot(x, normalized_y[1])
    # plt.show()

    # y = np.subtract(y_ref, y)

    # print('substracted dif : ' + file_to_compare + ' : ' + str(y[143]))

    # plt.plot(x[143], y[143], "xg")

    filtered = savgol_filter(y, 10, 3)
    noise = np.mean(abs(y - filtered))
    
    # print(noise)
    
    normalized_y = savgol_filter(normalized_y[0], 10, 3)

    peaks_x = []
    peaks_y = []

    # if should_find_peaks:
    # peaks, peaks_infos = find_peaks(y, prominence=0.03, width=12)
    # peaks = peaks[0]
    # print(peaks_infos)
        # peaks = np.array(peaks, dtype='i4')

    # if len(peaks) > 0:
    if True:
        # for peak in peaks:
            # print(peak)
        # peaks_x.append(x[peaks[0]])
        # peaks_y.append(y[peaks[0]])
            # print(y[peak])
        # print(file_to_compare)
        # left_plateau = y[int(peaks_infos['left_ips'][0])]

        # print(peaks_infos)

        # plateau_loc = find_plateau(y, peaks[0], peaks_y[0])
        # print(plateau_loc)

        # plt.plot(peaks_x, peaks_y, "ob")
        # plt.plot(x[plateau_loc], y[plateau_loc], "xr")
        # plt.vlines(x[peaks[0]], y[peaks[0]] - peaks_infos["prominences"][0], y[peaks[0]], color="gray", linestyle="dashed")
        # print(file_to_compare + ' : ' + str(peaks_y[0] - y[plateau_loc]))
        # print(file_to_compare + ' : ' + str(peaks_infos["prominences"][0]))
        # print(file_to_compare + ' : ' + str(peak_height/old_max))
        
        if 'ethanol' in file_to_compare:
            prominences.append(peak_height)
            prominences_down_noise.append(peak_height-noise)
            prominences_up_noise.append(peak_height+noise)
            if '100_' in file_to_compare or '_0_' in file_to_compare:
                plt.plot(x, normalized_y)
                
        else:
            # plt.vlines(x[peaks[0]], y[peaks[0]] - peak_height/old_max, y[peaks[0]], color="gray", linestyle="dashed")
            # plt.plot(x, normalized_y)
            alcools.append(peak_height)
            print(file_to_compare + ' ' + str(noise/peak_height))
            alcools_down_noise.append(peak_height-noise)
            alcools_up_noise.append(peak_height+noise)
        
        # plt.plot(x[int(peaks_infos['left_ips'][0])], y[int(peaks_infos['left_ips'][0])], "xr")
        # plt.plot(x[int(peaks_infos['right_ips'][0])], y[int(peaks_infos['right_ips'][0])], "xr")
        # print(file_to_compare + ' : ' + str(peaks_y[0] - left_plateau))
    else:
        prominences.append(0)
        prominences_down_noise.append(0)
        prominences_up_noise.append(0)
    # plt.plot(peaks[0], peaks[1])
    peaks_infos = {}
    
# plt.legend(['', '', ''] + files_to_compare)
plt.legend(['Éthanol', 'Eau'], loc=0, fontsize=15)
plt.xlabel(r"Nombre d'onde (cm$^{-1}$)", fontsize=15)
plt.ylabel('Intensité (relative)', fontsize=15)
plt.title('Spectre Raman des échantillons', fontsize=15)
plt.gca().invert_xaxis()
plt.savefig("waterEthanol.pdf")
plt.show()

def test_fitting(x, a, b, c):
    return a * x**2 + b * x + c
    
    
def invert_fitting(x, a, b, c):
    return (-b + np.sqrt(b**2 - 4 * a * (c - x)))/ (2 * a)
    

x = [100.0, 80.0, 60.0, 40.0, 20.0, 0.0]
y = prominences
y_down_noise = prominences_down_noise
y_up_noise = prominences_up_noise

# print(y_down_noise)
# print(y_up_noise)

param, param_cov = curve_fit(test_fitting, x, y)
param_down, param_cov_down = curve_fit(test_fitting, x, y_down_noise)
param_up, param_cov_up = curve_fit(test_fitting, x, y_up_noise)
# print(param)
ans = []
ans_down = []
ans_up = []
linear = np.linspace(0, 100)

for i in linear:
    ans.append(test_fitting(i, param[0], param[1], param[2]))
    ans_down.append(test_fitting(i, param_down[0], param_down[1], param_down[2]))
    ans_up.append(test_fitting(i, param_up[0], param_up[1], param_up[2]))


gin_bottom_left_percent = invert_fitting(alcools_down_noise[0], param_down[0], param_down[1], param_down[2])
gin_bottom_right_percent = invert_fitting(alcools_down_noise[0], param_up[0], param_up[1], param_up[2])
gin_top_right_percent = invert_fitting(alcools_up_noise[0], param_up[0], param_up[1], param_up[2])
gin_top_left_percent = invert_fitting(alcools_up_noise[0], param_down[0], param_down[1], param_down[2])

vodka_bottom_left_percent = invert_fitting(alcools_down_noise[1], param_down[0], param_down[1], param_down[2])
vodka_bottom_right_percent = invert_fitting(alcools_down_noise[1], param_up[0], param_up[1], param_up[2])
vodka_top_right_percent = invert_fitting(alcools_up_noise[1], param_up[0], param_up[1], param_up[2])
vodka_top_left_percent = invert_fitting(alcools_up_noise[1], param_down[0], param_down[1], param_down[2])

whisky_bottom_left_percent = invert_fitting(alcools_down_noise[2], param_down[0], param_down[1], param_down[2])
whisky_bottom_right_percent = invert_fitting(alcools_down_noise[2], param_up[0], param_up[1], param_up[2])
whisky_top_right_percent = invert_fitting(alcools_up_noise[2], param_up[0], param_up[1], param_up[2])
whisky_top_left_percent = invert_fitting(alcools_up_noise[2], param_down[0], param_down[1], param_down[2])

gin_percent = (-param[1] + np.sqrt(param[1]**2 - 4 * param[0] * (param[2] - alcools[0])))/ (2 * param[0])
vodka_percent = (-param[1] + np.sqrt(param[1]**2 - 4 * param[0] * (param[2] - alcools[1])))/ (2 * param[0])
whisky_percent = (-param[1] + np.sqrt(param[1]**2 - 4 * param[0] * (param[2] - alcools[2])))/ (2 * param[0])

print('gin : ', gin_percent)
print('vodka : ', vodka_percent)
print('whisky : ', whisky_percent)

fig, ax = plt.subplots()

ans_max = max(ans_up)

ans_up = ans_up/ans_max
ans_down = ans_down/ans_max
ans = ans/ans_max
alcools_down_noise = alcools_down_noise/ans_max
alcools_up_noise = alcools_up_noise/ans_max

# print(alcools)
# plt.plot(x, y, color='gray')
plt.plot(linear, ans_down, color='red', linestyle='dashed', label='_nolegend_')
plt.plot(linear, ans_up, color='green', linestyle='dashed', label='_nolegend_')
plt.plot(linear, ans, label='_nolegend_')
# plt.plot(gin_bottom_left_percent, alcools_down_noise[0], 'xb')
# plt.plot(gin_bottom_right_percent, alcools_down_noise[0], 'xb')
# plt.plot(gin_top_right_percent, alcools_up_noise[0], 'xb')
# plt.plot(gin_top_left_percent, alcools_up_noise[0], 'xb')

ax.add_patch(Polygon([(whisky_bottom_left_percent, alcools_down_noise[2]), (whisky_bottom_right_percent, alcools_down_noise[2]), (whisky_top_right_percent, alcools_up_noise[2]), (whisky_top_left_percent, alcools_up_noise[2])],
                                 hatch='', facecolor=(0,1,0,0.4)))

ax.add_patch(Polygon([(gin_bottom_left_percent, alcools_down_noise[0]), (gin_bottom_right_percent, alcools_down_noise[0]), (gin_top_right_percent, alcools_up_noise[0]), (gin_top_left_percent, alcools_up_noise[0])],
                                 hatch='/////', facecolor=(0,0,0,0)))

ax.add_patch(Polygon([(vodka_bottom_left_percent, alcools_down_noise[1]), (vodka_bottom_right_percent, alcools_down_noise[1]), (vodka_top_right_percent, alcools_up_noise[1]), (vodka_top_left_percent, alcools_up_noise[1])],
                                 hatch='\\\\', facecolor=(1,1,1,0)))

plt.plot([vodka_top_left_percent, vodka_top_right_percent], [alcools_up_noise[1], alcools_up_noise[1]], color='black', label=None)
plt.plot([vodka_bottom_left_percent, vodka_bottom_right_percent], [alcools_down_noise[1], alcools_down_noise[1]], color='black', label=None)

plt.plot([gin_top_left_percent, gin_top_right_percent], [alcools_up_noise[0], alcools_up_noise[0]], color='black', label=None)
plt.plot([gin_bottom_left_percent, gin_bottom_right_percent], [alcools_down_noise[0], alcools_down_noise[0]], color='black', label=None)

# print(gin_percent)
# print(vodka_percent)
# print(whisky_percent)
# plt.plot(gin_percent, alcools[0], 'xg')
# plt.plot(vodka_percent, alcools[1], 'xr')
# plt.plot(whisky_percent, alcools[2], 'xb')
# plt.hlines(alcools[0], 0, 100, color="gray", linestyle="dashed")
# plt.vlines(gin_percent, 2843, 3343, color="gray", linestyle="dashed")
# plt.vlines(vodka_percent, 2790, 3290, color="blue", linestyle="dashed")
# plt.vlines(whisky_percent, 2738, 3238, color="brown", linestyle="dashed")
# plt.errorbar(gin_percent, 2843, xerr=)
# plt.hlines(alcools[1], 0, 100, color="red", linestyle="dashed")
# plt.hlines(alcools[2], 0, 100, color="brown", linestyle="dashed")
# plt.axis([35, 45, 0.45, 0.7])

plt.legend(['Whisky', 'Gin', 'Vodka'], fontsize=15)
plt.xlabel('Pourcentage (%)', fontsize=15)
plt.ylabel('Intensité (relative)', fontsize=15)
plt.title("Intensité du spectre Raman selon le taux d'éthanol", fontsize=15)

plt.gca().invert_xaxis()


axins = zoomed_inset_axes(ax, 3, loc=3, borderpad=2)
# axins = ax.inset_axes(
#     [0.1, 0.1, 0.3, 0.3],
#     xlim=(35, 45), ylim=(0.45, 0.7))

axins.plot(linear, ans_down, color='red', linestyle='dashed', label='_nolegend_')
axins.plot(linear, ans_up, color='green', linestyle='dashed', label='_nolegend_')
axins.plot(linear, ans, label='_nolegend_', color=(0.12, 0.47, 0.7, 0.5))
    
axins.add_patch(Polygon([(whisky_bottom_left_percent, alcools_down_noise[2]), (whisky_bottom_right_percent, alcools_down_noise[2]), (whisky_top_right_percent, alcools_up_noise[2]), (whisky_top_left_percent, alcools_up_noise[2])],
                                 hatch='', facecolor=(0,1,0,0.4)))

axins.add_patch(Polygon([(gin_bottom_left_percent, alcools_down_noise[0]), (gin_bottom_right_percent, alcools_down_noise[0]), (gin_top_right_percent, alcools_up_noise[0]), (gin_top_left_percent, alcools_up_noise[0])],
                                 hatch='/////', facecolor=(0,0,0,0)))

axins.add_patch(Polygon([(vodka_bottom_left_percent, alcools_down_noise[1]), (vodka_bottom_right_percent, alcools_down_noise[1]), (vodka_top_right_percent, alcools_up_noise[1]), (vodka_top_left_percent, alcools_up_noise[1])],
                                 hatch='\\\\', facecolor=(1,1,1,0)))

axins.plot([vodka_top_left_percent, vodka_top_right_percent], [alcools_up_noise[1], alcools_up_noise[1]], color='black', label=None)
axins.plot([vodka_bottom_left_percent, vodka_bottom_right_percent], [alcools_down_noise[1], alcools_down_noise[1]], color='black', label=None)

axins.plot([gin_top_left_percent, gin_top_right_percent], [alcools_up_noise[0], alcools_up_noise[0]], color='black', label=None)
axins.plot([gin_bottom_left_percent, gin_bottom_right_percent], [alcools_down_noise[0], alcools_down_noise[0]], color='black', label=None)



axins.set_xlim(33, 47)
axins.set_ylim(0.5, 0.65)
axins.set_xticks([])
axins.set_yticks([])
mark_inset(ax, axins, loc1=1, loc2=4, fc="none", ec="0.5")

# axins = ax.inset_axes(
#     [0.1, 0.1, 0.5, 0.5],
#     xlim=(35, 45), ylim=(0.45, 0.7), xticklabels=[], yticklabels=[])

# axins.plot(x,y)

# ax.indicate_inset_zoom(axins, edgecolor="black")
plt.gca().invert_xaxis()
plt.savefig("percentComparison.pdf")

plt.show()