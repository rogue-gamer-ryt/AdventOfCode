from collections import Counter
from pathlib import Path

txt = Path('input.txt').read_text()

_input = txt.split('\n')

s = 0
prev = 0
for i in range(0, len(_input) + 1, 3):
    group = _input[prev:i]
    all_c = ''
    if group:
        g1, g2, g3 = set(group[0]), set(group[1]), set(group[2])
        common = list(g1.intersection(g2).intersection(g3))
        print(common)
        if common:
            common = common[0]
            num = ord(common)
            if 97 <= num <= 97 + 26:
                p = num - 96
            else:
                p = num - 64 + 26
            s += p
    prev = i
    # c1, c2 = set(line[:len(line) // 2]), set(line[len(line) // 2:])
    # common = list(c1.intersection(c2))
print(s)