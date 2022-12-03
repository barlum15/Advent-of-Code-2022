def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    score = 0

    for i in range(0, int(len(lines)/3)):
        duplicate = find_duplicate_char(lines[i*3], lines[(i*3)+1], lines[(i*3)+2])
        score += calculate_score_per_char(duplicate[0])

    print("Score: " + str(score))


def find_duplicate_char(string1, string2, string3):
    common_characters = []
    for char in string1:
        if char in string2:
            if char in string3:
                common_characters.append(char)

    return common_characters


def calculate_score_per_char(char):
    if 97 <= ord(char) <= 122:
        return ord(char) - 96
    if 65 <= ord(char) <= 90:
        return ord(char) - 38


main()
