data = open("input.txt").read().strip()

pos = 13
print()

for i in range(len(data)):
    temp_signal = data[i - 1:i + pos]
    if (len(set(temp_signal)) == 14):
        print(pos+i)
        break