import matplotlib.pyplot as plt
import numpy             as np
          

x = np.array([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

y = np.cos(x)

plt.plot(x, y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line Graph')
plt.savefig('plot.png')  # Save as PNG file
plt.show()
