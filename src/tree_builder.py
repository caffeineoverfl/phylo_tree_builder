from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

def build_tree(distance_matrix, method="nj"):
    constructor = DistanceTreeConstructor()
    if method == "upgma":
        return constructor.upgma(distance_matrix)
    else:
        return constructor.nj(distance_matrix)
