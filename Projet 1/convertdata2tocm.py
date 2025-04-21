import numpy as np

refFile = '11_03_ethanol_100_Reference_100sec_aligned_1.txt'

def open_file(file_to_compare):
    x = []
    y = []
    folder = './Data2/'
    if '11_03' in file_to_compare:
        folder = './DataRamanCM/'
        
    with open(folder + file_to_compare, 'r') as data:
        for line in data:
            p = line.split()
            currentPixel = float(p[0])
            # if currentPixel < 2000 and currentPixel > 800:
            x.append(float(p[0]))
            y.append(float(p[1]))
    return x, y


refx, refy = open_file(refFile)

files_to_convert = [
    ('15_04_ethanol_100_300sec_1.txt', 5110),
    ('15_04_ethanol_80_300sec_1.txt', 5007),
    ('15_04_ethanol_60_300sec_1.txt', 4099),
    ('15_04_ethanol_40_300sec_1.txt', 2955),
    ('15_04_ethanol_20_300sec_1.txt', 1532)
]


for file_to_convert, i in files_to_convert:
    
    x, y = open_file(file_to_convert)
    
    if '15_04' in file_to_convert:
        print('reversed')
        y = y[::-1]
            
    np.savetxt('Data2CM/' + file_to_convert, np.array([refx, y]).T)
        