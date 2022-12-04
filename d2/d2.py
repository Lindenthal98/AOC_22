"""
Enemy: My play
A:X Rock + 1
B:Y Paper +2
C:Z Scissor +3

0 Lost
3 Draw
6 Won

A Y
C X
B Y

"""

with open('input.txt', "r") as infile:
    data = [line.split() for line in infile]

loses_to = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

points_dict = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

matches_dict = {
    'A':'X',
    'B':'Y',
    'C':'Z'
}

# def sol(enemy_choice, my_choice):
#     if my_choice == loses_to[enemy_choice]:
#         print (f'win ${my_choice} {enemy_choice}')
#         points += points_dict[my_choice] + 6
#
#     elif my_choice == matches_dict[enemy_choice]:
#         print (f'draw ${my_choice} {enemy_choice}')
#
#     else:
#         print('loose')
    # elif (my_choice != loses_to[enemy_choice]) and (enemy_choice != loses_to[my_choice]):
    #     print (f'draw ${my_choice} {enemy_choice}')
    # else :
    #     print (f'lose ${my_choice} {enemy_choice}')

points = 0
for x in range(len(data)):
    if data[x][1] == loses_to[data[x][0]]:
        points += points_dict[data[x][1]] + 6

    elif data[x][1] == matches_dict[data[x][0]]:
        points += points_dict[data[x][1]] + 3

    else:
        points += points_dict[data[x][1]] + 0

print(points)