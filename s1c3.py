#!/usr/bin/python3

# Single-byte XOR cipher
# The hex encoded string:
# 
# 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character. Find the key, decrypt the message.
# 
# You can do this by hand. But don't: write code to do it for you.
# 
# How? Devise some method for "scoring" a piece of English plaintext. 
# Character frequency is a good metric. Evaluate each output and choose the one with the best score.

LETTER_FREQUENCIES = {
    'E' : 12.0,
    'T' : 9.10,
    'A' : 8.12,
    'O' : 7.68,
    'I' : 7.31,
    'N' : 6.95,
    'S' : 6.28,
    'R' : 6.02,
    'H' : 5.92,
    'D' : 4.32,
    'L' : 3.98,
    'U' : 2.88,
    'C' : 2.71,
    'M' : 2.61,
    'F' : 2.30,
    'Y' : 2.11,
    'W' : 2.09,
    'G' : 2.03,
    'P' : 1.82,
    'B' : 1.49,
    'V' : 1.11,
    'K' : 0.69,
    'X' : 0.17,
    'Q' : 0.11,
    'J' : 0.10,
    'Z' : 0.07,
    ' ' : 13.00 
}

def score_text(text):
    """Score a piece of text to determine how likely that this text is 'English'"""
    return sum([LETTER_FREQUENCIES.get(chr(c), 0) for c in text.upper()])


def attempt_xor(input, candidate):
    """Attempt to XOR string with candidate char"""
    
    output = b''
    for char in input:
        output += bytes([char ^ candidate])

    return output

if __name__ == "__main__":
    print('Set 1: Challenge 3: Cooking MC''s like a pound of bacon')
    input = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    
    candidates = []
    for i in range(256):
        message = attempt_xor(input, i)
        score = score_text(message)
        candidates.append(
            {
                'message': message,
                'score': score,
                'key': chr(i)
            }
        )

    print(sorted(candidates, key=lambda x: x['score'], reverse=True)[0])
