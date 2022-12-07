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
        from_stack_index = int(splited_line[3])-1
        to_stack_index = int(splited_line[5])-1
        length_from_stack = len(stacks[from_stack_index])
        # get values from stack and put them on other stack
        value_from_stack = stacks[from_stack_index][length_from_stack - int(splited_line[1]):length_from_stack]
        # remove values from stack
        del stacks[from_stack_index][length_from_stack - int(splited_line[1]):length_from_stack]
        # append each value to stack
        for item in value_from_stack:
            stacks[to_stack_index].append(item)

    print(stacks)


main()
