from matplotlib import pyplot as plt
x=[1,2,3,4]
y=[5,6,7,8]
plt.plot(x,y,color="red",linestyle="--",linewidth=2)
plt.grid(True)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Line Chart")
plt.show()