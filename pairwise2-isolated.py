from Bio import Align
from pathlib import Path

asequence = Path("000F.seq").read_text()
bsequence = Path("001F.seq").read_text()

aligner = Align.PairwiseAligner()
aligner.mode = "global"

aligner.open_gap_score = -10 
aligner.extend_gap_score = -0.5

alignments = aligner.align(asequence, bsequence)

for alignment in sorted(alignments):
    print("Score = %.1f:" % alignment.score)
    print(alignment)
