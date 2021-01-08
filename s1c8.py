#!/usr/bin/python3

# In this file are a bunch of hex-encoded ciphertexts.
# 
# One of them has been encrypted with ECB.
# 
# Detect it.
# 
# Remember that the problem with ECB is that it is stateless and deterministic; 
# the same 16 byte plaintext block will always produce the same 16 byte ciphertext.

import base64
from Crypto.Cipher import AES
from collections import Counter

def read_file(path):
    with open(path, 'rb') as file:
        return base64.b64decode(file.read())

def chunk(bytes, chunk_size):
    chunk_count = int(len(bytes) / chunk_size)
    for i in range(chunk_count):
        cur = i * chunk_size
        end = cur + chunk_size
        yield bytes[cur:end]


if __name__ == "__main__":
    print('Set 1: Challenge 8: Detect ECB ciphertext')
    cipherbytes = read_file('resources/s1c8.txt')
    chunked = chunk(cipherbytes, 16)
    counted = Counter(chunked)
    winner = counted.most_common(1)[0]

    bytes, count = winner[0], winner[1]
    print(f'Winner! This block occurs {count} time(s) in the text:')
    print(bytes)
