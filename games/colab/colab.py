"""
A collaborative grid world game

Reference: https://doi.org/10.1016/j.robot.2017.03.003
"""

from matplotlib import pyplot as plt
import numpy as np
import networkx as nx

class World:
    BLANK = 0
    OBSTACLE = 1

    ACTIONS = {
        "N": (0, 1),
        "S": (0, -1),
        "E": (1, 0),
        "W": (-1, 0)
    }

    def __init__(self, grid_size, obstacles, src, dst):
        self.grid_size = grid_size
        self.obstacles = obstacles
        self.src = src
        self.dst = dst

        self.board = nx.Graph()

        self.init()


    def init(self):
        self.board = nx.grid_2d_graph(self.grid_size,
                                      self.grid_size)

        for obstacle in self.obstacles:
            for direction in "NSEW":
                node = tuple(sum(x) for x in zip(self.index2pos(obstacle),
                                             World.ACTIONS[direction]))
                edge = (self.index2pos(obstacle), node)

                if self.is_valid_pos(node) and self.board.has_edge(*edge):
                    self.board.remove_edge(*edge)


    def reset(self):
        pass


    def index2pos(self, index):
        row = (index - 1) // self.grid_size
        col = (index - 1) - self.grid_size * row

        return row, col


    def pos2index(self, pos):
        row, col = pos

        return row * self.grid_size + col + 1


    def is_valid_pos(self, pos):
        row, col = pos
        return 0 <= row <= 9 and 0 <= col <= 9


    def is_mahattan(self, p1, p2):
        if abs(len(p1) - len(p2)) == 1:
            print("here")
            return True
        else:
            t_span = min(len(p1), len(p2))

            for t_step in range(t_span):
                (x1, y1), (x2, y2) = p1[t_step], p2[t_step]
                dist = abs(x2-x1) + abs(y2-y1)

                if dist == 1:
                    continue
                else:
                    return False

            return True


    def find_paths(self):
        src1, src2 = self.src
        dst1, dst2 = self.dst

        src_1 = self.index2pos(src1)
        dst_1 = self.index2pos(dst1)

        paths1 = list(nx.all_shortest_paths(self.board,
                                           source=src_1,
                                           target=dst_1))

        src_2 = self.index2pos(src2)
        dst_2 = self.index2pos(dst2)

        paths2 = list(nx.all_shortest_paths(self.board,
                                           source=src_2,
                                           target=dst_2))

        print(f"# of paths for agent 1: {len(paths1)}")
        print(f"# of paths for agent 2: {len(paths2)}")

        pruned_paths = []
        pruned_1 = set()
        pruned_2 = set()

        for p1 in paths1:
            for p2 in paths2:
                if self.is_mahattan(p1, p2):
                    pA = str(list(map(self.pos2index, p1)))
                    pB = str(list(map(self.pos2index, p2)))

                    pruned_paths.append((pA, pB))
                    pruned_1.add(str(pA))
                    pruned_2.add(str(pB))

        print(f"# of pruned path pairs: {len(pruned_paths)}")
        print(f"# of pruned paths for agent 1: {len(pruned_1)}")
        print(f"# of pruned paths for agent 2: {len(pruned_2)}")


    def show(self, paths=None):
        layout = nx.spectral_layout(self.board)

        for k in layout:
            layout[k] = k

        labels = dict()
        colors = list()

        for x in range(self.grid_size):
            for y in range(self.grid_size):
                labels[(x, y)] = self.pos2index((x, y))
                color = 'k'

                if self.pos2index((x, y)) == self.src[0]:
                    labels[(x, y)] = "S1"
                    color = 'r'
                if self.pos2index((x, y)) == self.src[1]:
                    labels[(x, y)] = "S2"
                    color = 'y'
                if self.pos2index((x, y)) == self.dst[0]:
                    labels[(x, y)] = "G1"
                    color = 'r'
                if self.pos2index((x, y)) == self.dst[1]:
                    labels[(x, y)] = "G2"
                    color = 'y'

                colors.append(color)


        nx.draw(self.board,
                labels=labels,
                with_labels=True,
                pos=layout,
                node_color=colors,
                node_shape='s',
                node_size=400,
                font_color='w',
                font_size=8,
                width=10)


        if paths is not None:
            pathA, pathB = paths
            pass

        plt.show()
        plt.close()


if __name__ == '__main__':
    dim = 10
    obstacles = [9, 27, 40, 46, 52, 54, 58, 61, 63, 67, 82, 85]

    src = [10, 20]
    goal = [91, 81]

    env = World(dim, obstacles, src, goal)
    env.show()
    # env.find_paths()
