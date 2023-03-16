import pandas as pd
from functions import *
from tkinter.filedialog import askopenfile

file = askopenfile(mode='r', title='Lütfen birleştirme bilgilerinin bulunduğu dosyayı seçin')
lines = file.readlines()

lines.remove(lines[0])

int_lines = []
for line in lines:
    line = line.replace("\n", "").split(",")
    int_line = [int(x) for x in line]
    int_lines.append(int_line)

distance_map = []
temp_list = []
Big_M = 999;
for i in range(len(lines)):
    temp_list = []
    for j in range(len(lines)):
        if i == j:
            temp_list.append(Big_M)
        else:
            temp_list.append(euclidian_dist(int_lines, i, j))
    distance_map.append(temp_list)

# Export to excel
df = pd.DataFrame(distance_map)
df.to_excel('distance_maps.xlsx', index=True)