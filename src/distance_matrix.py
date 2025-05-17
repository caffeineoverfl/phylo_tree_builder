from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator

def compute_distance_matrix(aligned_file):
    alignment = AlignIO.read(aligned_file, "fasta")
    calculator = DistanceCalculator('identity')  # or 'blosum62' for proteins
    return calculator.get_distance(alignment)
