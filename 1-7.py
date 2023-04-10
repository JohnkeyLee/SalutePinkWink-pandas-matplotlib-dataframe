import matplotlib.pyplot as plt
import numpy as np

plt.figure
plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0])
plt.show()

# This is to make an axis in 't' between '0' and '12', and it has '0.01' interval
t = np.arange(0,12,0.01)
# This is to plot the sin curve corresponding to 't' 
y = np.sin(t)
plt.figure(figsize=(10,6))
plt.plot(t,y)
plt.grid()
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Example of sinwave')
plt.show()

t = np.arange(0,12,0.01)
y = np.sin(t)
plt.figure(figsize=(10,6))
plt.plot(t, np.sin(t), lw=3, label='sin')
plt.plot(t, np.cos(t), 'r', label='cos')
plt.grid()
plt.legend()
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Example of sinwave')
plt.show()

plt.figure(figsize=(10,6))
plt.plot(t, np.sin(t), lw=3, label='sin')
plt.plot(t, np.cos(t), 'r', label='cos')
plt.grid()
plt.legend()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.ylim(-1.2, 1.2)
plt.xlim(0, np.pi)
plt.show()

# X-Y graph with markers
a = [0,1,2,3,4,5,6]
b = [1,4,5,8,9,5,3]
plt.figure(figsize=(10,6))
plt.plot(a,b, color='green', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
plt.xlim([-0.5, 6.5])
plt.ylim([0.5, 9.5])
plt.show()

# Scatter plot with colored bar
d = [0,1,2,3,4,5,6,7,8,9]
e = [9,8,7,9,8,3,2,4,3,4]
colormap = d
plt.figure(figsize=(10,6))
plt.scatter(d,e, s=50, c=colormap, marker='>',)
plt.colorbar()
plt.show()

# Here, 'loc' is for the average number and 'scale' is for standard deviation
s1 = np.random.normal(loc=0, scale=1, size=1000)
s2 = np.random.normal(loc=5, scale=0.5, size=1000)
s3 = np.random.normal(loc=10, scale=2, size=1000)
plt.figure(figsize=(10,6))
plt.plot(s1, label='s1')
plt.plot(s2, label='s2')
plt.plot(s3, label='s3')
plt.legend()
plt.show()
# Boxplot
plt.figure(figsize=(10,6))
plt.boxplot((s1,s2,s3))
plt.grid()
plt.show()

t = np.arange(0, 5, 0.5)
plt.figure(figsize=(10,6))
plt.plot(t, t, 'r--')
plt.plot(t, t**2, 'bs')
plt.plot(t, t**3, 'g^')
plt.show()