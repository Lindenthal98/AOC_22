data = open("input.txt").read().strip().split("\n")

overlap_count = 0

for pairing in data:
    elf_range_1, elf_range_2 = pairing.split(',')
    start_1, end_1 = [int(x) for x in elf_range_1.split('-')]
    start_2, end_2 = [int(x) for x in elf_range_2.split('-')]

    temp_range1 = range(start_1, end_1 + 1)
    temp_range2 = range(start_2, end_2 + 1)

    if (
            set(temp_range1) & set(temp_range2)
    ):
        overlap_count += 1

print(overlap_count)
