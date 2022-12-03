def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    score = 0

    for line in lines:
        first, second = splitstring(line)
        duplicate = find_duplicate_char(first, second)
        score += calculate_score_per_char(duplicate[0])

    print("Score: " + str(score))


def splitstring(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2


def find_duplicate_char(string1, string2):
    common_characters = []
    for char in string1:
        if char in string2:
            common_characters.append(char)

    return common_characters


def calculate_score_per_char(char):
    if 97 <= ord(char) <= 122:
        return ord(char) - 96
    if 65 <= ord(char) <= 90:
        return ord(char) - 38


main()
