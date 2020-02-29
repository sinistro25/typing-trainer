import matplotlib.pyplot as plt
import numpy as np
import pickle
def moving_average(series, n=10):
    tmp = np.cumsum(series)
    avg = np.zeros(series.shape)
    for i in range(n,len(series)):
        avg[i] = (tmp[i]-tmp[i-n]) / n
    for i in range(0,n):
        avg[i] = tmp[i]/(i+1)
    return avg

with open("log/wpm.txt","r") as file:
    wpm = file.readlines()
    wpm = np.array([float(x) for x in wpm])
with open("log/acc.txt","r") as file:
    acc = file.readlines()
    acc = np.array([100*float(x) for x in acc])
with open("log/key_latency.pkl","rb") as file:
    key_latency = pickle.load(file)
    for key, latencies in key_latency.items():
        if latencies != []:
            avg_lat = sum(latencies)/len(latencies)
        else:
            avg_lat = 0
        key_latency[key] = 100*avg_lat
x = [i for i in range(len(wpm))]

fig = plt.figure(figsize=(10,10))

plt.subplot(3,1,1)
plt.title("wpm")
plt.plot(x,wpm, color="red", label="wpm")
plt.plot(x,moving_average(wpm),color="green", label="wpm_avg")
plt.subplot(3,1,2)
plt.title("acc")
plt.plot(x,acc, color="red", label="acc")
plt.plot(x,moving_average(acc),color="green", label="acc_avg")
plt.subplot(3,1,3)
values = list(key_latency.values())
keys = [key for key in key_latency]
plt.bar(keys, values)
plt.show()
