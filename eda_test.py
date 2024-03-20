import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/mlb_data.csv")

print(df.head())

runs = df["R"]

hits = df["H"]


plt.plot(runs, hits)

plt.show()
