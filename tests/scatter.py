import matplotlib.pyplot as plt
import numpy as np

points = [[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]
x = [p[0] for p in points]
y = [p[1] for p in points]

plt.scatter(x, y)
plt.show()