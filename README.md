## Project Structure:

phylo_tree_builder/
├── data/                      # Raw and processed data
│   └── example.fasta          # Sample input
├── src/                       # Source code
│   ├── __init__.py
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
