def rna(dna):
    rna = dna.replace('T', 'U')
    return rna
    
print(rna("CCAGGACCAGGCCCCAGGTGGGGCCAGGCCAGGCTC"))