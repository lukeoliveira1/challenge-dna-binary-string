import os
from functions import (
    binary_to_dna_and_save,
    dna_to_binary_and_save,
    generate_dna,
    measure_performance,
)

if __name__ == "__main__":

    # for i in [100, 1000, 2500, 5000, 7500, 10000]:
    i = 100
    dna = generate_dna(i)

    time_codify, memory_used_codify, dna_codified = measure_performance(
        dna_to_binary_and_save, dna, "string/files/dna_binary.txt"
    )
    binary_file_size = os.path.getsize("string/files/dna_binary.txt")

    time_decodify, memory_used_decodify, dna_decodified = measure_performance(
        binary_to_dna_and_save, dna_codified, "string/files/dna.txt"
    )
    dna_file_size = os.path.getsize("string/files/dna.txt")

    print(f"Tamanho: {i}")
    print(f"Tempo para codificar: {time_codify:.6f}s")
    print(f"Memória usada para codificar: {memory_used_codify:.6f}MB")
    print(f"Tamanho do arquivo codificado(binário): {binary_file_size} bytes")
    print(f"Tempo para decodificar: {time_decodify:.6f}s")
    print(f"Memória usada para decodificar: {memory_used_decodify:.6f}MB")
    print(f"Tamanho do arquivo decofidicado(DNA): {dna_file_size} bytes\n\n")
