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
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

wins_over = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

points_dict = {
    'A': 1,
    'B': 2,
    'C': 3,
}

ending_dict = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

matches_dict = {
    'A':'A',
    'B':'B',
    'C':'C'
}


points = 0
for x in range(len(data)):
    enemy_choice = data[x][0]
    match_ending = data[x][1]

    if match_ending == 'X': #loose
        points += points_dict[wins_over[enemy_choice]] + ending_dict[match_ending]
    elif match_ending == 'Y': #draw
        points += points_dict[matches_dict[enemy_choice]] + ending_dict[match_ending]
    else:
        points += points_dict[loses_to[enemy_choice]] + ending_dict[match_ending]


print(points)