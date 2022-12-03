from pathlib import Path

txt = Path('input.txt').read_text()

_input = txt.split('\n\n')

max_s = float('-inf')
each_elf = []
for line in _input:
    each_elf_total = sum([int(x) for x in line.split()])
    each_elf.append(each_elf_total)
    max_s = max(max_s, each_elf_total)
print(max_s)
each_elf.sort(reverse=True)
print(sum(each_elf[:3]))
