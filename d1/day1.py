food_per_elf = []
cal_per_elf = []


with open('input.txt', "r") as infile:
    data = [line.split() for line in infile]

temp_array = []
for food in data:
    if len(food) == 0:

        food_per_elf.append(sum(temp_array))
        temp_array = []
        continue

    temp_array.append(int(food[0]))

food_per_elf.sort()

print(food_per_elf[-1])
print(sum(food_per_elf[len(food_per_elf)-3:]))
