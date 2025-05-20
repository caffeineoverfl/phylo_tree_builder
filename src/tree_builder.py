# Builds a phylogenetic tree using UPGMA or Neighbor Joining

from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

def build_tree(distance_matrix, method="nj"):
    constructor = DistanceTreeConstructor()
    if method == "upgma":
        return constructor.upgma(distance_matrix)
    else:
        return constructor.nj(distance_matrix)

def build_tree_upgma(alignment_file, output_tree_file="output/tree.nwk"):

    aln = AlignIO.read(alignment_file, "fasta")
    calculator = DistanceCalculator("identity")
    dm = calculator.get_distance(aln)

    constructor = DistanceTreeConstructor()
    tree = constructor.upgma(dm)

    Phylo.write(tree, output_tree_file, "newick")
    return output_tree_file
