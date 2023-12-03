import re
import math

# first task
with open("input.txt") as file:
    ids_sum = 0
    limits = {"red": 12, "green": 13, "blue": 14}
    for line in file:
        if line[-1] == '\n':
            line = line[:-1]
        game_id, game_vals = line.split(': ')
        values_list = re.split(", |; ", game_vals)
        for val in values_list:
            count, color = val.split()
            if int(count) > limits[color]:
                break
        else:
            ids_sum += int(game_id.split()[1])
    print(ids_sum)  # Your puzzle answer was 2528


# second task
with open("input.txt") as file:
    power_sum = 0
    for line in file:
        min_limits = {"red": 0, "green": 0, "blue": 0}
        if line[-1] == '\n':
            line = line[:-1]
        _, game_vals = line.split(': ')
        values_list = re.split(", |; ", game_vals)
        for val in values_list:
            count, color = val.split()
            count = int(count)
            if count > min_limits[color]:
                min_limits[color] = count
        power_sum += math.prod(min_limits.values())
    print(power_sum)  # Your puzzle answer was 67363


