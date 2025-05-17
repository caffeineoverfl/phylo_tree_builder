from src import parser, aligner, distance_matrix, tree_builder, visualizer

def main():
    input_fasta = "data/example_dna.fasta"
    aligned = aligner.run_clustal_omega(input_fasta)
    dist_matrix = distance_matrix.compute_distance_matrix(aligned)
    tree = tree_builder.build_tree(dist_matrix)
    visualizer.visualize_tree(tree)

if __name__ == "__main__":
    main()
