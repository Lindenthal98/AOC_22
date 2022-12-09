data = open("input.txt").read().strip()

pos = 3
print()

for i in range(len(data)):
    curr_chunk = data[i - 1:i + pos]
    if (len(set(curr_chunk)) == 4):
        print(pos+i)
        break