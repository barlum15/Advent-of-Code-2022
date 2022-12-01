def calculate_calories():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    max_calories = 0
    sum_calories = 0
    for line in lines:
        if line and line.strip():
            sum_calories += int(line)
            if sum_calories > max_calories:
                max_calories = sum_calories
        else:
            sum_calories = 0
    print("Max calories: " + str(max_calories))


def main():
    calculate_calories()

main()

