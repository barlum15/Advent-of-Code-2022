def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    n = 9
    stacks = [[] for i in range(n)]
    score = 0
    empty_entry_index = lines.index("\n")

    for line in reversed(lines[0:empty_entry_index - 1]):
        for i in range(8, -1, -1):
            if line[4*i] != " ":
                stacks[i].append(line[4*i+1])

    for line in lines[empty_entry_index + 1:len(lines)]:
        splited_line = line.split(" ")
        for i in range(0, int(splited_line[1])):
            value = stacks[int(splited_line[3])-1].pop()
            stacks[int(splited_line[5])-1].append(value)

    print(stacks)


main()
