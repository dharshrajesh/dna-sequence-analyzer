# DNA Sequence Analyzer

def validate_sequence(seq):
    for base in seq:
        if base not in "ATCG":
            return False
    return True


def gc_content(seq):
    g = seq.count("G")
    c = seq.count("C")
    return ((g + c) / len(seq)) * 100


def reverse_complement(seq):
    complement = ""

    for base in seq:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "C":
            complement += "G"
        elif base == "G":
            complement += "C"

    return complement[::-1]


def nucleotide_count(seq):
    return {
        "A": seq.count("A"),
        "T": seq.count("T"),
        "C": seq.count("C"),
        "G": seq.count("G")
    }


# Main Program
dna = input("Enter DNA sequence: ").upper()

if not validate_sequence(dna):
    print("Invalid DNA sequence! Only A, T, C, G allowed.")
else:
    print("\n--- DNA Analysis Results ---")
    
    print("Length:", len(dna))
    
    counts = nucleotide_count(dna)
    print("Nucleotide Count:", counts)
    
    print("GC Content: {:.2f}%".format(gc_content(dna)))
    
    print("Reverse Complement:", reverse_complement(dna))