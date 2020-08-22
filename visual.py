import matplotlib.pyplot as plt
from test import RandomWalk

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
ax.scatter(0, 0, c = 'green', edgecolors = 'none', s=20)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 20)
plt.show()