import time
import matplotlib.pyplot as plt
voltage=[1.18,1.26,1.32,1.36,1.37,1.39,1.41,1.42,1.43,1.44,1.46,1.46,1.47,1.47,1.48]
amps=[1.25,0.92,0.72,0.59,0.31,0.45,0.40,0.36,0.33,0.30,0.23,0.22,0.21,0.20,0.19]
L=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]
R=[]
sumr=0
print(len(voltage))
print(len(amps))
print(len(L))
for x in range(len(voltage)):
    R.append(voltage[x]/amps[x])
print(R)
for x in range(len(R)):
    sumr=sumr+R[x]
print(sumr/len(R))
plt.plot(L,R)
plt.plot(L,voltage)
plt.plot(L,amps)
plt.ylabel('Resistance / Voltage / Amps')
plt.xlabel('Lenth')
plt.legend()
plt.show()
