from Bio import Align
from pathlib import Path
from Bio.Align import substitution_matrices

# Load the NUC.4.4 substitution matrix
nuc44_matrix = substitution_matrices.load("NUC.4.4")

# Read sequences from files
asequence = Path("000F.seq").read_text().strip()
bsequence = Path("001F.seq").read_text().strip()

# Define valid characters
valid_chars = set("ACGTN")

# Clean sequences
asequence = ''.join([char for char in asequence if char in valid_chars])
bsequence = ''.join([char for char in bsequence if char in valid_chars])

# Initialize the aligner
aligner = Align.PairwiseAligner()
aligner.mode = "global"
aligner.open_gap_score = -10 
aligner.extend_gap_score = -0.5
aligner.substitution_matrix = nuc44_matrix

# Perform the alignment
alignments = aligner.align(asequence, bsequence)
print(alignments[0])
