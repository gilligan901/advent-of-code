from day_2_input import real_input as input


param_red = 12
param_green = 13
param_blue = 14

id = 0
sum_of_ids = 0
for line in input.splitlines():
    id += 1 
    split_line = line.split(": ")
    games = split_line[1].split("; ")
    fails = 0
    for game in games:
        red = 0
        green = 0
        blue = 0
        cubes = game.split(", ")
        for cube in cubes:
            amount = int(cube.split(" ")[0])
            if cube.find("red") != -1:
                red = amount
            elif cube.find("green") != -1:
                green = amount
            elif cube.find("blue") != -1:
                blue = amount
        if (red > param_red or green > param_green or blue > param_blue):
            fails += 1
    if (fails == 0):
        sum_of_ids += id

print(sum_of_ids)



        



