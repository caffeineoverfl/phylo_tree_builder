# Phylogenetic Tree Builder (still in development)
A Python tool to build and visualize phylogenetic trees from DNA or protein sequences. This project takes FASTA files, performs sequence alignment, constructs evolutionary trees using algorithms like UPGMA or Neighbor Joining, and renders them as static or interactive visualizations.

## Project Structure: <br>

```bash
phylo_tree_builder/<br>
├── data/                      # Raw and processed data 
│   └── example.fasta          # Sample input 
├── src/                       # Source code 
│   ├── __init__.py <br>
│   ├── parser.py              # FASTA input parser 
│   ├── aligner.py             # Handles sequence alignment 
│   ├── distance_matrix.py     # Builds distance matrix 
│   ├── tree_builder.py        # Tree construction algorithms 
│   └── visualizer.py          # Static/interactive tree visualization
├── tests/                     # Unit tests
├── docs/                      # Project documentation
├── requirements.txt           # Project dependencies
├── README.md                  # Project overview and usage instructions
└── main.py                    # CLI entry point
```
