# -- IMPORTS ----------------------------------------------------------------

from collections import defaultdict
from math import ceil

# TODO have to install colorama
# to make guesses easier to see
from colorama import Fore, Style, init
init()

# -- PARAMS -----------------------------------------------------------------

KEYWORD_SIZE = 17
"""
JEW gap: 51
YTD gap: 17
NZF gap: 85

keyword: can only be 17
"""

CIPHER_FILE = 'ciphertext.txt'

# -- START ------------------------------------------------------------------

with open(CIPHER_FILE, 'r') as f:
    original = f.read()

alpha = []

for c in original:
    if c.isalpha():
        alpha.append(c)

alpha = ''.join(alpha)

counter = defaultdict(lambda: 0)
mention = set()

for sublen in range(3, 10):
    for start in range(len(alpha) - sublen + 1):
        key = alpha[start:start + sublen]
        counter[key] += 1
        if counter[key] > 1:
            mention.add(key)

lst = []

for w in mention:
    lst.append([counter[w], w])

lst.sort(key=lambda t: t[0])

print('\n'.join([f'{t[1]}: {t[0]}' for t in lst]))
print()


RESET = Style.RESET_ALL

def trans(color, word):
    return Style.RESET_ALL + Style.BRIGHT + color + word + RESET


subs = {
    # 'JEW': ('AND', Fore.RED),
    # 'NZF': ('ART', Fore.CYAN),
    # 'YTD': ('THE', Fore.YELLOW),
    # 'XYX': ('POO', Fore.BLUE),
    'RMMO': ('MANY', Fore.GREEN),
    'ZKE': ('HOW', Fore.GREEN)
}

original_guess = original
alpha_guess = alpha
alpha_no_color = alpha

for old, (new, color) in subs.items():

    shift_nums = [
        (ord(o) - ord(n)) % 26
        for o, n in zip(old, new)
    ]

    shift_chars = [chr(ord('A') + n) for n in shift_nums]

    shifts = ' '.join(shift_chars)

    print(f'shifting {old} to {new} ({shifts})')

    original_guess = original_guess.replace(old, trans(color, new) + Style.DIM)
    alpha_guess = alpha_guess.replace(old, trans(color, new) + Style.DIM)
    alpha_no_color = alpha_no_color.replace(old, f'<{new}>')

print()
print(Style.RESET_ALL + 'Punctuation')

print(Style.DIM + original_guess)

# print(Style.RESET_ALL + 'No punctuation')
# print(Style.DIM + alpha_guess)

print()
print(Style.RESET_ALL + 'Chunks')
print(Style.DIM, end='')

ctr = 0
buf = []

for c in alpha_no_color:
    buf.append(c)

    if not c.isalpha() and c != '.':
        if c == '<':
            buf.pop()
            buf.append(Style.NORMAL)
        elif c == '>':
            buf.pop()
            buf.append(Style.DIM)

        continue

    ctr += 1

    if ctr == KEYWORD_SIZE:
        print(''.join(buf) + Style.NORMAL + Fore.RED + '|' + Style.RESET_ALL + Style.DIM, end='')
        buf.clear()
        ctr = 0

print()


# -- GUESSING ---------------------------------------------------------------

keyword = """
XVFERTQXSWIFMZQAB
"""

"""
ABCDEFGHIJKLMNOPQRSTUVWXYZ
"""

keyword = keyword.replace('\n', '')

assert len(keyword) == KEYWORD_SIZE, 'wrong keyword size'

print()
print(Style.RESET_ALL + 'Keyword Guess')

ctr = 0

buf = []

dimmed = False

buf.append(Style.RESET_ALL)

for c in original:

    if not c.isalpha():
        buf.append(c)
        continue

    shift_char = keyword[ctr % KEYWORD_SIZE]

    # print(f'shift {c} by {shift_char}')

    if shift_char == '.':
        if not dimmed:
            buf.append(Style.DIM)
            dimmed = True
        buf.append(c)
    else:
        if dimmed:
            buf.append(Style.NORMAL)
            dimmed = False
        shift = ord(shift_char) - ord('A')
        buf.append(chr((ord(c) - ord('A') - shift) % 26 + ord('A')))

    ctr += 1

print(Style.DIM, end='')
print(''.join(buf))
