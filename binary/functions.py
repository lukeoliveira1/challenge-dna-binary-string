###################
# coding to binary
###################

dna_codify = {"A": 0b00, "C": 0b01, "G": 0b10, "T": 0b11}


def dna_to_binary(dna):
    binary = 0b0
    for letter in dna:
        binary = (binary << 2) | dna_codify[letter]
    return binary


def save_to_binary(binary_data, filename):
    with open(filename, "wb") as file:
        num_bytes = (
            binary_data.bit_length() + 7
        ) // 8  # discover the number of bytes needed to store the binary data
        file.write(binary_data.to_bytes(num_bytes, byteorder="big"))


def dna_to_binary_and_save(dna, filename):
    binary = dna_to_binary(dna)
    save_to_binary(binary, filename)
    return binary


#####################
# decoding to string
#####################


dna_decoding = {0b00: "A", 0b01: "C", 0b10: "G", 0b11: "T"}


def binary_to_dna(binary_data, length):
    dna = ""
    for _ in range(length):
        dna = dna_decoding[binary_data & 0b11] + dna
        binary_data >>= 2
    return dna


def save_to_dna(dna, filename):
    with open(filename, "w") as file:
        file.write(dna)


def binary_to_dna_and_save(binary_data, length, filename):
    dna = binary_to_dna(binary_data, length)
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
