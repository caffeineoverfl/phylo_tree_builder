# Reads a FASTA file and returns a dictionary of {sequence_id: sequence_string}

from Bio import SeqIO

def read_fasta(filepath):
    sequences = list(SeqIO.parse(filepath, "fasta"))
    return {record.id: str(record.seq) for record in sequences}
