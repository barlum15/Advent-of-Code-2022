def main():
    with open("input.txt", "r") as f:
        line = f.readlines()

    for index in range(len(line[0])):
        substring = line[0][index:index + 14]
        if len(set(substring)) == len(substring):
            print(index + 14)
            break


main()
