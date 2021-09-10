import matplotlib as mpl
import matplotlib as plt

def plotNodePosition(nodes):
    global W1; global W2; global wdelta

    number_of_node = print(nodes.shape[1])

    plt.plot([wdelta, W1], [wdelta, wdelta])
    plt.plot([W1, W1], [wdelta, W2])
    plt.plot([W1, wdelta], [W2, W2])
    plt.plot([wdelta, wdelta], [W2, wdelta])