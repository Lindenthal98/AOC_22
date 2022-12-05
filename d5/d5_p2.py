import re

def parse_stack_text(stacktext):
    stacks = [""] * 10
    for line in stacktext[:-1]:
        for i, box in enumerate(line[1::4]):
            if box != " ": stacks[i + 1] += box
    return stacks


input_data = open("input.txt").read()
stackt, instructions = [part.split("\n") for part in input_data.split("\n\n")]
stacks = parse_stack_text(stackt)[1:]

mda_stack = [[*col ]for col in stacks]
for col in mda_stack:
    col.reverse()

for instr in instructions:
    crate_amount, current_dest, next_dest = [int(x) for x in re.findall('[0-9]+', instr)]

    selected_crates = mda_stack[current_dest-1][-crate_amount:]
    del mda_stack[current_dest-1][-crate_amount:]
    mda_stack[next_dest-1].extend(selected_crates)



sol = ''

for col in mda_stack:
    sol += col.pop()

print(sol)
