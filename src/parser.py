from Bio import SeqIO

def read_fasta(filepath):
    sequences = list(SeqIO.parse(filepath, "fasta"))
    return {record.id: str(record.seq) for record in sequences}
