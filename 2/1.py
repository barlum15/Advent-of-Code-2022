import pandas as pd

def main():
    input = pd.read_csv('input.txt', sep=" ", header=None)
    input.columns = ['oponent', 'mine']

    input.oponent.values
    input.mine.values

    score = 0
    for i in range(0, len(input.oponent.values)):
        if input.mine.values[i] == 'X':
            score += 1
        elif input.mine.values[i] == 'Y':
            score += 2
        elif input.mine.values[i] == 'Z':
            score += 3

        if input.mine.values[i] == 'X' and input.oponent.values[i] == 'C' or\
                input.mine.values[i] == 'Y' and input.oponent.values[i] == 'A' or\
                input.mine.values[i] == 'Z' and input.oponent.values[i] == 'B':
            score += 6
        elif input.mine.values[i] == 'X' and input.oponent.values[i] == 'A' or\
                input.mine.values[i] == 'Y' and input.oponent.values[i] == 'B' or\
                input.mine.values[i] == 'Z' and input.oponent.values[i] == 'C':
            score += 3

    print("Score: " + str(score))

main()