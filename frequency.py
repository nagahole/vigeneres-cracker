from collections import Counter
from math import ceil
import matplotlib.pyplot as plt

import os

with open('ciphertext.txt', 'r') as f:
    cipher = f.read()

alpha = []

for c in cipher:
    if c.isalpha():
        alpha.append(c)

alpha = ''.join(alpha)

KEYWORD_SIZE = 17
n_chunks = ceil(len(alpha) / KEYWORD_SIZE)

# make sure output folder exists
os.makedirs("frequencies", exist_ok=True)

shifts = {
    0: 23,
    1: 21,
    2: 5,
    3: 4,
    4: 17,
    5: 19,
    6: 20,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0,
    14: 0,
    15: 0,
    16: 0,
}

for i in range(17):
    print(chr(ord('A') + shifts[i]), end='')

print()

for of in range(KEYWORD_SIZE):

    shift = shifts[of]

    freq = {}

    for i in range(26):
        c = chr(ord('A') + i)

        freq[c] = 0

    for ch in range(n_chunks):
        idx = ch * KEYWORD_SIZE + of

        if idx >= len(alpha):
            continue

        c = alpha[idx]

        after = chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
        freq[after] += 1


    # sort by character for consistent x-axis
    items = sorted(freq.items())
    letters, counts = zip(*items)

    # plot
    plt.figure()
    plt.bar(letters, counts)
    plt.title(f"Offset {of} frequency, shifted by {shift}")
    plt.xlabel("Character")
    plt.ylabel("Count")

    # save
    plt.savefig(f"frequencies/offset_{of}.png")
    plt.close()
