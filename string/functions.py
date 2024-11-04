###################
# coding to binary
###################

dna_codify = {"A": "00", "C": "01", "G": "10", "T": "11"}


def dna_to_binary(dna):
    binary = ""
    for letter in dna:
        binary += dna_codify[letter]
    return binary


def save_to_binary(binary, filename):
    with open(filename, "w") as file:
        file.write(binary)


def dna_to_binary_and_save(dna, filename):
    binary = dna_to_binary(dna)
    save_to_binary(binary, filename)
    return binary


#####################
# decoding to string
#####################

dna_decodify = {"00": "A", "01": "C", "10": "G", "11": "T"}


def binary_to_dna(binary):
    dna = ""
    for i in range(0, len(binary), 2):
        dna += dna_decodify[binary[i : i + 2]]
    return dna


def save_to_dna(binary, filename):
    with open(filename, "w") as file:
        file.write(binary)


def binary_to_dna_and_save(binary_data, filename):
    dna = binary_to_dna(binary_data)
    save_to_dna(dna, filename)
    return dna


###############
# generate dna
###############

import random


def generate_dna(length):
    dna = ""
    for _ in range(length):
        dna += random.choice("ACGT")
    return dna


##########
# measure
##########


import time
import os
import psutil


def measure_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # Retorna o uso de memória em MB


def measure_performance(func, *args):
    start_time = time.time()
    memory_before = measure_memory()
    result = func(*args)
    memory_after = measure_memory()
    end_time = time.time()
    execution_time = end_time - start_time
    memory_used = memory_after - memory_before
    return execution_time, memory_used, result
