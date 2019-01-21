from copy import deepcopy
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os


BOARD_DIM = 3
BETA = 0.99
REWARD = 100

AGENT_A_POSITION = 0
AGENT_B_POSITION = BOARD_DIM - 1

graph = nx.Graph()
graph.add_nodes_from(range(0, BOARD_DIM**2))

edges = [(0,1), (0,3), (1,2), (1,4), (2,5), (3,6), (3,4), (4,5), (4,7),
        (5,8), (6,7), (7,8)]

graph.add_edges_from(edges)


def index2pos(index):
    row = index % BOARD_DIM
    col = index // BOARD_DIM

    return np.array([row, col])


def show_graph(graph, agentA, agentB, goalA, goalB):
    layout = nx.spectral_layout(graph)
    for k in layout:
        layout[k] = index2pos(k)

    labels = dict((n, n) for n in range(BOARD_DIM**2))
    labels[agentA] = "A"
    labels[agentB] = "B"
    labels[goalA] = "gA"
    labels[goalB] = "gB"

    nx.draw(graph, labels=labels, with_labels=True, pos=layout)
    plt.show()
    plt.close()


def print_graph(graph, agentA, agentB, goalA, goalB, pathA, pathB, name):
    G = deepcopy(graph)

    layout = nx.spectral_layout(graph)
    for k in layout:
        layout[k] = index2pos(k)

    labels = dict((n, n) for n in range(BOARD_DIM**2))
    labels[agentA] = "A"
    labels[agentB] = "B"
    labels[goalA] = "gA"
    labels[goalB] = "gB"

    nx.draw_networkx_nodes(G, pos=layout, node_color='k')
    nx.draw_networkx_labels(G, pos=layout, labels=labels, font_color='w')

    colors = ['k', 'g', 'y']
    linewidths = [1, 8, 4]

    routeA, routeB = [], []

    for idx in range(len(pathA)-1):
        routeA.append((pathA[idx], pathA[idx+1]))

    for idx in range(len(pathB)-1):
        routeB.append((pathB[idx], pathB[idx+1]))


    routes = [edges, routeA, routeB]

    for ctr, edgelist in enumerate(routes):
        nx.draw_networkx_edges(G,
                               pos=layout,
                               edgelist=edgelist,
                               edge_color= colors[ctr],
                               width=linewidths[ctr])

    plt.axis('off')

    plt.legend(["Nodes", "Edges", "Agent A", "Agent B"],
               fontsize='x-small',
               markerscale=0.1,
               loc=(0, 0))

    ticks = [-0.5, 0.5, 1.5, 2.5]

    for tick in ticks:
        plt.axvline(tick,
                    color='grey',
                    alpha=0.8,
                    linewidth=0.5,
                    zorder=-10)
        plt.axhline(tick,
                    color='grey',
                    alpha=0.8,
                    linewidth=0.5,
                    zorder=-10)

    plt.savefig(os.path.join("traversals", name),
                bbox_inches='tight',
                transparent=True,
                dpi=200)
    plt.close()


def discounted_return(path):
    exp = len(path)-1

    return (BETA ** exp) * REWARD



if __name__ == '__main__':
    goalA, goalB = BOARD_DIM**2 - 1, BOARD_DIM**2 - BOARD_DIM
    agentA, agentB = AGENT_A_POSITION, AGENT_B_POSITION

    pathsA = list(nx.all_simple_paths(graph, source=agentA, target=goalA))
    pathsB = list(nx.all_simple_paths(graph, source=agentB, target=goalB))

    non_colliding_paths = []


    for pA in pathsA:
        for pB in pathsB:
            shorter_length = min(len(pA), len(pB))

            pA_ = pA[:shorter_length+1]
            pB_ = pB[:shorter_length+1]

            colliding = False

            for t_step in range(shorter_length):
                if pA_[t_step] == pB_[t_step]:
                    colliding = True
                    break

            if not colliding:
                non_colliding_paths.append((pA, pB))

    with open("non_colliding_paths.txt", "w") as fp:
        fp.write("Non Colliding Paths\n")

        for idx, paths in enumerate(non_colliding_paths):
            a, b = paths
            name = f"game #{idx+1}.png"

            print_graph(graph, agentA, agentB, goalA, goalB, a, b, name)

            returnA = discounted_return(a)
            returnB = discounted_return(b)

            fp.write(f"\nPath #{idx+1}\n")

            fp.write(":: Agent A ::\n")
            fp.write(f"Path = {a}\n")
            fp.write(f"Discounted Return = {returnA}\n")

            fp.write(":: Agent B ::\n")
            fp.write(f"Path = {b}\n")
            fp.write(f"Discounted Return = {returnB}\n")

    # show_graph(graph, agentA, agentB, goalA, goalB)
