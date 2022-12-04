from collections import Counter

# lines = open("inputs/3.txt").read().strip().split("\n")

with open('input.txt', "r") as infile:
    data = [line.split() for line in infile]

priority_sum = 0

# dict gernerator
values_lower = {chr(i): i + 1 - 97 for i in range(ord("a"), ord("a") + 26)}
values_upper = {chr(i): i + 1 - 39 for i in range(ord("A"), ord("A") + 26)}

values_dict = values_lower | values_upper

for backpack in range(len(data)):
    backpack_content = data[backpack][0]

    compart_1 = backpack_content[:len(backpack_content)//2]
    compart_2 = backpack_content[len(backpack_content)//2:]

    # priority_sum += values_dict[list(set(compart_1) & set(compart_2))[0]]
    priority_sum += values_dict[list(set(compart_1) & set(compart_2)).pop()]


print(priority_sum)