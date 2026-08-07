import statistics
import matplotlib.pyplot as plt
estimates=[]
for i in range(100,1000,4):
    estimates.append(i)
print(estimates)
tv=int(0.1*(len(estimates)))
estimates=estimates[tv:]
estimates=estimates[:len(estimates)-tv]
y=[]
for i in range(len(estimates)):
    y.append(5)
plt.plot(estimates,y,'r--')
plt.plot([statistics.mean(estimates)],[y],'g^')
plt.plot([statistics.median(estimates)],[y],'ro')
plt.ylabel("time")
plt.xlabel("values")