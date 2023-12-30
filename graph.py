import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import figure
import numpy as np
df = pd.read_csv("DataSources/FinalData.csv", on_bad_lines='warn',sep=",", encoding="latin1")

data = pd.DataFrame(data = df)

data.plot.scatter(x="City Population", y="Award")


plt.show()