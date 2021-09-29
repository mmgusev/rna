def to_rna(dna_strand):
    dna_strand=str(dna_strand)
    dna_strand=dna_strand.replace("A", "U")
    dna_strand=dna_strand.replace("C", "g")
    dna_strand=dna_strand.replace("G", "c")
    dna_strand=dna_strand.replace("T", "A")
    dna_strand=dna_strand.replace("c", "C")
    dna_strand=dna_strand.replace("g", "G")
    return dna_strand
