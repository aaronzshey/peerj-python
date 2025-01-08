from Bio import Align
from pathlib import Path

from Bio.Align import substitution_matrices
nuc44_matrix = substitution_matrices.load("NUC.4.4")
print(nuc44_matrix)

asequence = Path("000F.seq").read_text()
bsequence = Path("001F.seq").read_text()

aligner = Align.PairwiseAligner()
aligner.mode = "global"

aligner.open_gap_score = -10 
aligner.extend_gap_score = -0.5
aligner.substitution_matrix = nuc44_matrix

alignments = aligner.align(asequence, bsequence)
print(alignments[0])

'''
for alignment in sorted(alignments):
    print("Score = %.1f:" % alignment.score)
    print(alignment)
'''
