import numpy as np

data = np.loadtxt('data.txt')

# part 1 
col0 = np.sort(data[:,0])
col1 = np.sort(data[:,1])
distance = np.abs(col0 - col1).sum().astype(int)
print(f"\n Total Distance = {distance}\n")

# part 2
score = 0
for number in col0:
    multiple = np.where(number == col1, 1, 0).sum()
    score += number * multiple
print(f"\n Total Score = {score.astype(int)}\n")