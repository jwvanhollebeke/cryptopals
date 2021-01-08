#!/usr/bin/python3

# The Base64-encoded content in this file has been encrypted via AES-128 in ECB mode under the key
# 
# "YELLOW SUBMARINE".
# (case-sensitive, without the quotes; exactly 16 characters; I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too).
# 
# Decrypt it. You know the key, after all.
# 
# Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.

import base64
from Crypto.Cipher import AES

def read_file(path):
    with open(path, 'rb') as file:
        return base64.b64decode(file.read())

def decipher(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext).decode('utf-8')

if __name__ == "__main__":
    print('Set 1: Challenge 7 -- YELLOW SUBMARINE')
    plaintext = decipher(read_file('resources/s1c7.txt'), b'YELLOW SUBMARINE')
    print(plaintext)
