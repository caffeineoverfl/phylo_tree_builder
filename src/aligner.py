# Runs Clustal Omega via subprocess to perform multiple sequence alignment

import subprocess

def run_clustal_omega(input_file, output_file="aligned.fasta"):
    subprocess.run([
        "clustalo", "-i", input_file, "-o", output_file, "--force"
    ])
    return output_file