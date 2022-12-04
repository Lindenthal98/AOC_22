from collections import Counter

with open('input.txt', "r") as infile:
    data = [line.split() for line in infile]

priority_sum = 0
grouped_list = []

# dict gernerator
values_lower = {chr(i): i + 1 - 97 for i in range(ord("a"), ord("a") + 26)}
values_upper = {chr(i): i + 1 - 39 for i in range(ord("A"), ord("A") + 26)}

values_dict = values_lower | values_upper

for i in range(0, len(data), 3):
    grouped_list.append(data[i:i+3])


for elves_backpack in grouped_list:

    temp_set = [set(elves_backpack[0][0]), set(elves_backpack[1][0]), set(elves_backpack[2][0])]
    badge_group = set.intersection(*temp_set)
    priority_sum += values_dict[list(badge_group)[0]]


print(priority_sum)


