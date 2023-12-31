import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure
import numpy as np
df = pd.read_csv("DataSources/FinalData.csv", on_bad_lines='warn',sep=",", encoding="latin1")

data = pd.DataFrame(data = df)


data.plot.scatter(x="Price Level", y="Award", alpha=0.3)

plt.yticks(np.arange(min(data["Award"]), max(data["Award"])+1, 1))
plt.xticks(np.arange(min(data["Price Level"]), max(data["Price Level"])+1, 1))
plt.ticklabel_format(style='plain')

plt.show()