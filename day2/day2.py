import numpy as np
import pandas as pd

# Part 1
df = pd.read_csv('data.txt', header=None)

data = df.values
data = [np.array(row[0].split()).astype(int) for row in data]

trend = [row[1:] - row[:-1] for row in data]
test1 = np.array([(report > 0).all()+(report < 0).all() for report in trend])
test2 = np.array([(np.abs(report).max() <= 3)*(np.abs(report).min() >= 1) for report in trend])
safe = test1*test2

print(f"\nTotal Number of Safe Reports = {safe.sum()}\n")
