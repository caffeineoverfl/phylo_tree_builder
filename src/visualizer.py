# Draws the tree using Biopython and matplotlib

from Bio import Phylo
import matplotlib.pyplot as plt

def visualize_tree(tree, output_file=None):
    Phylo.draw(tree)
    if output_file:
        plt.savefig(output_file)
    plt.show()
