with open("input.txt") as file:
    input_list = [list(line.rstrip('\n')) for line in file]


# first task
def test_part_number(i, j):
    if not input_list[i][j].isdigit():
        return False
    test_vals = [str(i) for i in range(10)] + ['.']
    if i > 0 and input_list[i-1][j] not in test_vals:
        return True
    if i < len(input_list)-1 and input_list[i+1][j] not in test_vals:
        return True
    if j > 0 and input_list[i][j-1] not in test_vals:
        return True
    if j < len(input_list[0])-1 and input_list[i][j+1] not in test_vals:
        return True
    if i > 0 and j > 0 and input_list[i-1][j-1] not in test_vals:
        return True
    if i < len(input_list)-1 and j < len(input_list[0])-1 and input_list[i+1][j+1] not in test_vals:
        return True
    if i < len(input_list)-1 and j > 0 and input_list[i+1][j-1] not in test_vals:
        return True
    if i > 0 and j < len(input_list[0])-1 and input_list[i-1][j+1] not in test_vals:
        return True
    return False


part_number_sum = 0
for i, l in enumerate(input_list):
    number = 0
    is_part_number = False
    little_sum = 0
    for j, elem in enumerate(l[::-1]):
        if elem.isdigit():
            little_sum += int(elem) * 10 ** number
            number += 1
            if not is_part_number:
                is_part_number = test_part_number(i, len(input_list[0])-1-j)
        else:
            if is_part_number:
                part_number_sum += little_sum
            number = 0
            is_part_number = False
            little_sum = 0
    if is_part_number:
        part_number_sum += little_sum

print(part_number_sum)  # Your puzzle answer was 553825


# second task
def gear_test(i, j):
    if not input_list[i][j].isdigit():
        return False
    test_vals = ['*']
    if i > 0 and input_list[i-1][j] in test_vals:
        return i-1, j
    if i < len(input_list)-1 and input_list[i+1][j] in test_vals:
        return i+1, j
    if j > 0 and input_list[i][j-1] in test_vals:
        return i, j-1
    if j < len(input_list[0])-1 and input_list[i][j+1] in test_vals:
        return i, j+1
    if i > 0 and j > 0 and input_list[i-1][j-1] in test_vals:
        return i-1, j-1
    if i < len(input_list)-1 and j < len(input_list[0])-1 and input_list[i+1][j+1] in test_vals:
        return i+1, j+1
    if i < len(input_list)-1 and j > 0 and input_list[i+1][j-1] in test_vals:
        return i+1, j-1
    if i > 0 and j < len(input_list[0])-1 and input_list[i-1][j+1] in test_vals:
        return i-1, j+1
    return False


gear_sum = 0
gears = {(i, j): False for i in range(len(input_list)) for j in range(len(input_list[0])) if input_list[i][j] == '*'}
for i, l in enumerate(input_list):
    number = 0
    little_sum = 0
    is_gear_number = False
    for j, elem in enumerate(l[::-1]):
        if elem.isdigit():
            little_sum += int(elem) * 10 ** number
            number += 1
            if not is_gear_number:
                is_gear_number = gear_test(i, len(input_list[0])-1-j)
        else:
            if is_gear_number:
                if gears[is_gear_number] is not False:
                    gear_sum += little_sum * gears[is_gear_number]
                else:
                    gears[is_gear_number] = little_sum
            number = 0
            little_sum = 0
            is_gear_number = False
    if is_gear_number:
        if gears[is_gear_number] is not False:
            gear_sum += little_sum * gears[is_gear_number]
        else:
            gears[is_gear_number] = little_sum

print(gear_sum)  # Your puzzle answer was 93994191


