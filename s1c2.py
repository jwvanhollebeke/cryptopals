#!/usr/bin/python3

# Fixed XOR
# 
# Write a function that takes two equal-length buffers and produces their XOR
# combination.
# 
# If your function works properly, then when you feed it the string:
# 
# 1c0111001f010100061a024b53535009181c
# 
# ... after hex decoding, and when XOR'd against:
# 
# 686974207468652062756c6c277320657965
# 
# ... should produce:
# 
# 746865206b696420646f6e277420706c6179

def xor_strings(b1, b2):
    """XOR two strings"""
    if len(b1) != len(b2):
        raise ValueError('Two strings not of equal length')
    return bytes([a ^ b for a,b in zip(b1, b2)])


if __name__ == "__main__":
    print('Set 1: Challenge 2: The kid don''t play')
    s1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
    s2 = bytes.fromhex('686974207468652062756c6c277320657965')
    print(xor_strings(s1, s2) == bytes.fromhex('746865206b696420646f6e277420706c6179'))