# Draws the tree using Biopython and matplotlib

from ete3 import Tree, TreeStyle
from Bio import Phylo
import matplotlib.pyplot as plt

def visualize_tree(tree, output_file=None):
    Phylo.draw(tree)
    if output_file:
        plt.savefig(output_file)
    plt.show()

def visualize_tree_interactive(newick_file):
    """
    Load and display a tree interactively using ETE3.
    """
    tree = Tree(newick_file, format=1)

    ts = TreeStyle()
    ts.show_leaf_name = True
    ts.title.add_face("Phylogenetic Tree", column=0)

    # You can customize node appearances here
    ts.show_branch_length = True
    ts.show_branch_support = True

    tree.show(tree_style=ts)

