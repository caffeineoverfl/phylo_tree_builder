from src import parser, aligner, distance_matrix, tree_builder, visualizer

def main():
    input_fasta = "data/example_dna.fasta"

    # use the parser module
    sequences = parser.read_fasta(input_fasta)
    print(f"Loaded {len(sequences)} sequences:")
    for seq_id, sequence in sequences.items():
        print(f"  {seq_id}: {len(sequence)} bp")

    # Run alignment
    aligned = aligner.run_clustal_omega(input_fasta)
    dist_matrix = distance_matrix.compute_distance_matrix(aligned)
    tree_newick = tree_builder.build_tree_upgma(aligned)
    visualizer.visualize_tree_interactive(tree_newick)

if __name__ == "__main__":
    main()
