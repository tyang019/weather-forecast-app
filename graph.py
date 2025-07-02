import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [40.2, 41.8, 47.4, 56.3, 65, 71.3, 78.5, 79.5, 73.6, 64.3, 54.2, 44.4]
plt.plot(x, y, marker='*')
plt.bar(x, y, width=0.5, color='red')
plt.title('Average Temperature Per Month in the US')
plt.xlabel('Month')
plt.ylabel('Temperature (°F)')
plt.grid(True)
plt.show()

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = [2, 2, 4, 4, 5, 11, 8, 6, 7, 5, 2, 2]
plt.plot(x, y, color='green')
plt.bar(x, y)
plt.xlabel('Month')
plt.ylabel('Precipitation/ Rainfall (inches)')
plt.title("Average Precipitation in the US per Month")
plt.show()