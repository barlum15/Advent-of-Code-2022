import numpy as np


def check_visibility_fixed_yi(iteration_range, yi, tree_grid, tree_height):
    is_visible = True
    for x in iteration_range:
        if tree_grid[x, yi] >= tree_height:
            is_visible = False
            break
    return is_visible


def check_visibility_fixed_xi(iteration_range, xi, tree_grid, tree_height):
    is_visible = True
    for y in iteration_range:
        if tree_grid[xi, y] >= tree_height:
            is_visible = False
            break
    return is_visible


def is_tree_visible(tree_grid, tree_height, xi, yi, matrix_length):
    if (xi == 0 or xi == matrix_length - 1 or yi == 0 or yi == matrix_length - 1) or \
            check_visibility_fixed_yi(range(xi - 1, -1, -1), yi, tree_grid, tree_height) or \
            check_visibility_fixed_yi(range(xi + 1, matrix_length), yi, tree_grid, tree_height) or \
            check_visibility_fixed_xi(range(yi - 1, -1, -1), xi, tree_grid, tree_height) or \
            check_visibility_fixed_xi(range(yi + 1, matrix_length), xi, tree_grid, tree_height) is True:
        return True
    else:
        return False


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    two_d_tree_grid = np.array([list(line.strip()) for line in lines])

    visible_trees = 0
    matrix_length = two_d_tree_grid.shape[0]

    for xi, yi in np.ndindex(matrix_length, matrix_length):
        tree_height = two_d_tree_grid[xi, yi]

        if is_tree_visible(two_d_tree_grid, tree_height, xi, yi, matrix_length):
            visible_trees += 1

    print("Trees visible: " + str(visible_trees))


main()
