import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    point_numberrs = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numberrs, cmap=plt.cm.Blues, edgecolors="none", s = 15)
    plt.show()

    keep_running = input("Make anthor walk? (y/n):")
    if keep_running == "n":
        break