import matplotlib
from matplotlib import pyplot as plt
from shapely.geometry import LinearRing, Polygon
from shapely.affinity import rotate
from math import pi


class BoxPushingGame:
    def __init__(self):
        self.bounds = [(0, 0), (0, 100), (100, 100), (100, 0)]
        self.boundary = Polygon(self.bounds)
        self.xbound, self.ybound = self.boundary.exterior.xy

        # width, height
        self.dimensions = [12, 4]

        # cx, cy, theta
        self.box = (15, 15, 90)
        self.target = (85, 80, 150)

    def render(self):
        fig, ax = plt.subplots()

        ax.plot(self.xbound,
                 self.ybound,
                 color='#000000',
                 linewidth=2,
                 zorder=2)

        dw, dh = self.dimensions

        cx, cy, theta = self.box
        x, y = cx - dw/2, cy - dh/2
        box = matplotlib.patches.Rectangle((x, y),
                                           dw,
                                           dh,
                                           theta,
                                           color="#4bb239")
        ax.add_patch(box)


        cx, cy, theta = self.target
        x, y = cx - dw/2, cy - dh/2
        box = matplotlib.patches.Rectangle((x, y),
                                           dw,
                                           dh,
                                           theta,
                                           color="#d83636")
        ax.add_patch(box)


        ax.axis("auto")
        ax.set_title("Box Pushing Game")
        plt.axis('off')

        plt.show()


if __name__ == '__main__':
    game = BoxPushingGame()
    game.render()
