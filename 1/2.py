def calculate_calories():
    with open("input.txt", "r") as f:
        lines = f.readlines()
    max_calories_1 = 0
    max_calories_2 = 0
    max_calories_3 = 0
    sum_calories = 0
    for line in lines:
        if line and line.strip():
            sum_calories += int(line)
        else:
            if sum_calories > max_calories_1:
                max_calories_3 = max_calories_2
                max_calories_2 = max_calories_1
                max_calories_1 = sum_calories
                sum_calories = 0
            elif sum_calories > max_calories_2 and max_calories_2 < max_calories_1:
                max_calories_2 = sum_calories
                max_calories_3 = max_calories_2
                sum_calories = 0
            elif sum_calories > max_calories_3 and max_calories_3 < max_calories_2 < max_calories_1:
                max_calories_3 = sum_calories
                sum_calories = 0
            else:
                sum_calories = 0
    print("Max calories: " + str(max_calories_1 + max_calories_2 + max_calories_3))


def main():
    calculate_calories()

main()

