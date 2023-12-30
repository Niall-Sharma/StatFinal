import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure
import numpy as np
dt = pd.read_csv("DataSources/FinalData.csv", on_bad_lines='warn',sep=",", encoding="latin1")

Level4 = [0,0,0]
Level3 = [0,0,0]
Level2 = [0,0,0]
Level1 = [0,0,0]

for index, row in dt.iterrows(): 
    if dt.loc[index, "Price Level"] == 4:
        if dt.loc[index, "Award"] == 3:
            Level4[2]+=1
        if dt.loc[index, "Award"] == 2:
            Level4[1]+=1
        if dt.loc[index, "Award"] == 1:
            Level4[0]+=1
    if dt.loc[index, "Price Level"] == 3:
        if dt.loc[index, "Award"] == 3:
            Level3[2]+=1
        if dt.loc[index, "Award"] == 2:
            Level3[1]+=1
        if dt.loc[index, "Award"] == 1:
            Level3[0]+=1
    if dt.loc[index, "Price Level"] == 2:
        if dt.loc[index, "Award"] == 3:
            Level2[2]+=1
        if dt.loc[index, "Award"] == 2:
            Level2[1]+=1
        if dt.loc[index, "Award"] == 1:
            Level2[0]+=1
    if dt.loc[index, "Price Level"] == 1:
        if dt.loc[index, "Award"] == 3:
            Level1[2]+=1
        if dt.loc[index, "Award"] == 2:
            Level1[1]+=1
        if dt.loc[index, "Award"] == 1:
            Level1[0]+=1

print(f"LEVEL 4: {Level4}\n LEVEL 3: {Level3}\n LEVEL 2: {Level2}\n LEVEL 1: {Level1}")

Awards = [Level1[1],Level2[1],Level3[1],Level4[1]]
print(Awards)
# plt.plot(np.array([1,4]), Awards)
# plt.show()  