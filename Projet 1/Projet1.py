import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks


def find_plateau(points, peak_index, peak_y):
    plateaued = False
    last = peak_y
    index = 0
    for i in points[peak_index:]:
        print(abs(i - last))
        if abs(i - last) < 100:
            if plateaued:
                return peak_index - index
            else:
                plateaued = True
        else:
            plateaued = False
        last = i
        index += 1
    return 0

files_to_compare = [
    '11_03_ethanol_100_Reference_100sec_aligned_1.txt',
    '11_03_ethanol_80_Reference_100sec_1.txt',
    '11_03_ethanol_60_Reference_100sec_1.txt',
    # '11_03_ethanol_40_Reference_100sec_1.txt',
    # '11_03_ethanol_20_Reference_100sec_1.txt',
    '11_03_ethanol_0_Reference_100sec_1.txt',
    # '11_03_gin_Reference_100sec_1.txt',
]


for file_to_compare in files_to_compare:
    
    x = []
    y = []
    with open('./DataRamanCM/' + file_to_compare, 'r') as data:
        for line in data:
            p = line.split()
            currentPixel = float(p[0])
            if currentPixel < 2000 and currentPixel > 800:
                x.append(float(p[0]))
                y.append(float(p[1]))

    peaks_x = []
    peaks_y = []

    # if should_find_peaks:
    peaks, peaks_infos = find_peaks(y, width=12)
    # peaks = peaks[0]
    # print(peaks_infos)
        # peaks = np.array(peaks, dtype='i4')

    if len(peaks) > 0:
        for peak in peaks:
            peaks_x.append(x[peak])
            peaks_y.append(y[peak])

        # left_plateau = y[int(peaks_infos['left_ips'][0])]

        # print(peaks_infos)

        plateau_loc = find_plateau(y, peaks[0], peaks_y[0])
        print(plateau_loc)

        plt.plot(peaks_x[0], peaks_y[0], "ob")
        plt.plot(x[plateau_loc], y[plateau_loc], "xr")
        # plt.plot(x[int(peaks_infos['left_ips'][0])], y[int(peaks_infos['left_ips'][0])], "xr")
        # plt.plot(x[int(peaks_infos['right_ips'][0])], y[int(peaks_infos['right_ips'][0])], "xr")
        # print(file_to_compare + ' : ' + str(peaks_y[0] - left_plateau))
        
    # plt.plot(peaks[0], peaks[1])
    plt.plot(x, y)
    peaks_infos = {}
    
# plt.legend(['', '', ''] + files_to_compare)
    plt.gca().invert_xaxis()
    plt.show()
