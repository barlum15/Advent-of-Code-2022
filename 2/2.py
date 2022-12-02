import pandas as pd

def main():
    input = pd.read_csv('input.txt', sep=" ", header=None)
    input.columns = ['oponent', 'mine']

    input.oponent.values
    input.mine.values

    score = 0
    for i in range(0, len(input.oponent.values)):
        if input.mine.values[i] == 'X':
            score += 0
        elif input.mine.values[i] == 'Y':
            score += 3
        elif input.mine.values[i] == 'Z':
            score += 6

        if input.oponent.values[i] == 'A':
            if input.mine.values[i] == 'X':
                score += 3
            elif input.mine.values[i] == 'Y':
                score += 1
            elif input.mine.values[i] == 'Z':
                score += 2
        elif input.oponent.values[i] == 'B':
            if input.mine.values[i] == 'X':
                score += 1
            elif input.mine.values[i] == 'Y':
                score += 2
            elif input.mine.values[i] == 'Z':
                score += 3
        elif input.oponent.values[i] == 'C':
            if input.mine.values[i] == 'X':
                score += 2
            elif input.mine.values[i] == 'Y':
                score += 3
            elif input.mine.values[i] == 'Z':
                score += 1

    print("Score: " + str(score))

main()