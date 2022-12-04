def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    score = 0

    for line in lines:
        first, second = splitstring(line)
        score += find_assignment(first, second)

    print("Score: " + str(score))


def splitstring(value):
    string1, string2 = value.split(",")
    return string1, string2


def find_assignment(first_assignment, second_assignment):
    first_assignment_start, first_assignment_end = first_assignment.split("-")
    second_assignment_start, second_assignment_end = second_assignment.split("-")
    if int(first_assignment_start) in range(int(second_assignment_start), int(second_assignment_end)+1) or\
            int(first_assignment_end) in range(int(second_assignment_start), int(second_assignment_end)+1) or\
            int(second_assignment_start) in range(int(first_assignment_start), int(first_assignment_end)+1) or\
            int(second_assignment_end) in range(int(first_assignment_start), int(first_assignment_end)+1):
        return 1
    else:
        return 0


main()
