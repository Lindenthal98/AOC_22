
data = open("input.txt").read().strip().split("\n")
grid = []

data = [str(x) for x in data]



def bigger_tree_present(lst, val):
    return (any(x >= int(val) for x in lst))


for row in range(len(data)):
    grid.append([])
    for col in range(len(data[row])):


        grid[row].append(data[row][col])

cnt = 0
for y in range(len(grid)):
    if y == 0 or y == len(grid) - 1:  # if upper/lower bound
        cnt += len(grid[y])
        continue
    for x in range(len(grid)):  # if edges
        if x == 0 or x == len(grid[x]) - 1:
            cnt += 1
            continue

        col = [sublist[x] for index, sublist in enumerate(grid) if index % 1 == 0]
        col.pop(y)

        col = [int(x) for x in col]
        row = [int(x) for x in grid[y]]
        row.pop(x)

        trees_above, trees_below = col[:y], col[y:]

        trees_left, trees_right = row[:x], row[x:]
        if (
                (bigger_tree_present(trees_above, grid[y][x]) and
                 bigger_tree_present(trees_below, grid[y][x])) and
                (bigger_tree_present(trees_left, grid[y][x]) and
                 bigger_tree_present(trees_right, grid[y][x]))

        ):

            continue
        cnt += 1

print(cnt)
