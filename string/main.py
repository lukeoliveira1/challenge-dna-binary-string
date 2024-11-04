from utils import dna

from functions import binary_to_dna, dna_to_binary

if __name__ == "__main__":
    dna_codified = dna_to_binary(dna)
    print(dna_codified)

    dna_decodified = binary_to_dna(dna_codified)
    print(dna_decodified)
