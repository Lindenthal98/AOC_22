import math

data = open("input.txt").read().strip().split("\n")
grid = []

data = [str(x) for x in data]



def smaller_tree_count(lst, val, direction):
    temp_count = 0
    if direction == 'forward':
        for x in lst:
            temp_count += 1
            if x >= int(val): break


    if direction == 'backwards':
        for x in reversed(lst):
            temp_count += 1
            if x >= int(val): break

    return temp_count


for row in range(len(data)):
    grid.append([])
    for col in range(len(data[row])):

        grid[row].append(data[row][col])

max_points = 0
for y in range(len(grid)):
    if y == 0 or y == len(grid) - 1:  # if upper/lower bound
        continue
    for x in range(len(grid)):  # if edges
        if x == 0 or x == len(grid[x]) - 1:
            continue

        col = [sublist[x] for index, sublist in enumerate(grid) if index % 1 == 0]
        col.pop(y)

        col = [int(x) for x in col]
        row = [int(x) for x in grid[y]]
        row.pop(x)

        trees_above, trees_below = col[:y], col[y:]
        trees_left, trees_right = row[:x], row[x:]

        top_view = smaller_tree_count(trees_above, grid[y][x], 'backwards')
        bot_view = smaller_tree_count(trees_below, grid[y][x], 'forward')
        left_view = smaller_tree_count(trees_left, grid[y][x], 'backwards')
        right_view = smaller_tree_count(trees_right, grid[y][x], 'forward')

        view_points = math.prod([top_view, bot_view, left_view, right_view])
        if view_points > max_points: max_points = view_points



print(max_points)
