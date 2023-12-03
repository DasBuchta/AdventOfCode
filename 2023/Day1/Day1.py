# first task
with open("input.txt") as file:
    whole_sum = 0
    for line in file:
        for char in line:
            if char.isdigit():
                whole_sum += 10*int(char)
                break
        for char in line[::-1]:
            if char.isdigit():
                whole_sum += int(char)
                break

    print(whole_sum)  # Your puzzle answer was 54916

# second task
with open("input.txt") as file:
    digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9} | {
        str(i): i for i in range(10)}
    whole_sum = 0
    for line in file:
        rev_line = line[::-1]
        minimal = len(line)
        maximal = len(rev_line)
        for digit, digit_value in digits.items():
            first_index = line.find(digit)
            last_index = rev_line.find(digit[::-1])
            if 0 <= first_index < minimal:
                first = digit_value
                minimal = first_index
            if 0 <= last_index < maximal:
                last = digit_value
                maximal = last_index
        if minimal < len(line):
            whole_sum += 10*first
        if maximal < len(line):
            whole_sum += last
    print(whole_sum)  # Your puzzle answer was 54728

