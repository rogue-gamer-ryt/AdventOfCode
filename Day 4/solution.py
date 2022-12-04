from pathlib import Path

txt = Path('input.txt').read_text()

_input = txt.split('\n')

count = 0

for p in _input:
    p1, p2 = p.split(',')
    p1, p2 = set(range(int(p1.split('-')[0]),
                       int(p1.split('-')[1]) + 1)), set(
                           range(int(p2.split('-')[0]),
                                 int(p2.split('-')[1]) + 1))
    # if p1.intersection(p2) == p1 or p1.intersection(p2) == p2:
    if p1.intersection(p2):
        count += 1

print(count)