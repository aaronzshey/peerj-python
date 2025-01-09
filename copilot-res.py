from Bio import Align
from pathlib import Path
from Bio.Align import substitution_matrices

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

'''
print(alignment)
GAACT
||--|
GA--T

alignment.aligned
(((0, 2), (4, 5)), ((0, 2), (2, 3)))

note how this tells us the fifth element of the target sequence (4, 5)
is aligned to the third element of the query sequence (2, 3)

We find the tuple with the greatest difference, representing the longest 
chunk of perfect alignment.

We also arbitrarily pick the first alignment, because it probably is the best one
'''
aligned = alignments[0].aligned

# convert alignemnts into diffs
coord_diffs = list(map(lambda x: int(x[1] - x[0]), aligned[0]))
# find index of greatest diff in coords, indicating longest excellent alignment
# chunk
max_diff_index = coord_diffs.index(max(coord_diffs))

# get left bounds from target (first aligned array) and query (second aligned array)

print(aligned[0][max_diff_index][0])
print(aligned[1][max_diff_index][0])




# Find chunks of 50 excellent alignments


