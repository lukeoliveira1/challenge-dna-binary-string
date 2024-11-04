import os

from utils import dna

from functions import binary_to_dna, dna_to_binary, save_to_binary, save_to_dna

dna = "ATCGTCGAT"

if __name__ == "__main__":

    ##########
    # codify
    ##########

    dna_codified = dna_to_binary(dna)
    # print(dna_codified)

    binary_file_path = "binary/files/dna.bin"
    save_to_binary(dna_codified, binary_file_path)  # 2 bytes

    binary_file_size = os.path.getsize(binary_file_path)
    print(f"File size: {binary_file_size} bytes")

    ##########
    # decodify
    ##########

    dna_decodified = binary_to_dna(dna_codified, len(dna))
    # print(dna_decodified)

    dna_file_path = "binary/files/dna.txt"
    save_to_dna(dna_decodified, dna_file_path)  # 9 bytes

    dna_file_size = os.path.getsize(dna_file_path)
    print(f"File size: {dna_file_size} bytes")
