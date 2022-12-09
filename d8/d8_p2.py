import math

data = open("input.txt").read().strip().split("\n")
grid = []
# data = [x for x in str(data)]
# print(data)
data = [str(x) for x in data]


# valid = 0
# print(data)
# #

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
        # print(data[row][col])
        # print(str(data)[row][col])

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
        # print(trees_above, trees_below, grid[y][x])

        trees_left, trees_right = row[:x], row[x:]
        # print(trees_left, trees_right, grid[y][x])
        top_view = smaller_tree_count(trees_above, grid[y][x], 'backwards')
        bot_view = smaller_tree_count(trees_below, grid[y][x], 'forward')
        left_view = smaller_tree_count(trees_left, grid[y][x], 'backwards')
        right_view = smaller_tree_count(trees_right, grid[y][x], 'forward')

        view_points = math.prod([top_view, bot_view, left_view, right_view])
        if view_points > max_points: max_points = view_points


# print([sublist[4] for index, sublist in enumerate(grid) if index % 1 == 0])

# for y in range(len(data)):
#     cnt += 1
#
#     if y == 0 or y == len(data)-1: continue
#     for x in range(len(str(data[y]))):
#         loop += 1
#
#         if x == 0 or x == len(str(data[y]))-1: continue
#         if (
#             data[x][y] < data[x][y+1] and
#             data[x][y] < data[x][y-1] and
#             data[x][y] < data[x+1][y] and
#             data[x][y] < data[x-1][y]
#
#
#         ):
#             print('not vis')
#         # print(data[y][x])
#
# print(cnt)
# print(loop)
print(max_points)
