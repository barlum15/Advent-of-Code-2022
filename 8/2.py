import numpy as np

highest_tree_score = 0


def calculate_distance_yi_fixed(iteration_range, xi, yi, tree_grid):
    distance = 0
    for x in iteration_range:
        if tree_grid[yi, xi] <= tree_grid[yi, x]:
            distance += 1
            break
        else:
            distance += 1
    return distance


def calculate_distance_xi_fixed(iteration_range, xi, yi, tree_grid):
    distance = 0
    for y in iteration_range:
        if tree_grid[yi, xi] <= tree_grid[y, xi]:
            distance += 1
            break
        else:
            distance += 1
    return distance


def is_tree_visible(tree_grid, xi, yi, matrix_length):
    global highest_tree_score
    distance_left = calculate_distance_yi_fixed(range(xi - 1, -1, -1), xi, yi, tree_grid)
    distance_right = calculate_distance_yi_fixed(range(xi + 1, matrix_length), xi, yi, tree_grid)
    distance_top = calculate_distance_xi_fixed(range(yi - 1, -1, -1), xi, yi, tree_grid)
    distance_bottom = calculate_distance_xi_fixed(range(yi + 1, matrix_length), xi, yi, tree_grid)

    current_tree_score = distance_left * distance_right * distance_top * distance_bottom
    if current_tree_score > highest_tree_score:
        highest_tree_score = current_tree_score


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    two_d_tree_grid = np.array([list(line.strip()) for line in lines])
    matrix_length = two_d_tree_grid.shape[0]

    for yi, xi in np.ndindex(matrix_length, matrix_length):
        is_tree_visible(two_d_tree_grid, xi, yi, matrix_length)

    print("Max score of tree: " + str(highest_tree_score))


main()
