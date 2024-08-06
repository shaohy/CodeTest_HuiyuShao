def reverse_list(l: list):
    """
    The function should return a sorted list.

    Input l is a list which can contain any type of data.

    """

    start = 0
    end = len(l) - 1
    while start < end:
        l[start], l[end] = l[end], l[start]
        start += 1
        end -= 1
    return l


# example_list = [1, 2, 3, 4, 5]
# print(reverse_list(example_list))


def solve_sudoku(matrix):
    """
    Sudoku is one of the most popular puzzle games of all time. The goal of Sudoku is to fill a 9×9 grid with numbers
    so that each row, column and 3×3 section contain all of the digits between 1 and 9. As a logic puzzle,
    Sudoku is also an excellent brain game.

    The input matrix is a 9x9 matrix. You need to write a program to solve it.

    """

    def dfs(pos):
        nonlocal is_solved
        if pos == len(empty_cells):
            is_solved = True
            return

        row, col = empty_cells[pos]
        for num in range(9):
            if not (row_check[row][num] or col_check[col][num] or block_check[row // 3][col // 3][num]):

                row_check[row][num] = col_check[col][num] = block_check[row // 3][col // 3][num] = True
                matrix[row][col] = str(num + 1)
                dfs(pos + 1)
                if is_solved:
                    return

                row_check[row][num] = col_check[col][num] = block_check[row // 3][col // 3][num] = False
                matrix[row][col] = "."

    row_check = [[False] * 9 for _ in range(9)]
    col_check = [[False] * 9 for _ in range(9)]
    block_check = [[[False] * 9 for _ in range(3)] for _ in range(3)]
    is_solved = False
    empty_cells = []

    for r in range(9):
        for c in range(9):
            if matrix[r][c] == ".":
                empty_cells.append((r, c))
            else:
                num = int(matrix[r][c]) - 1
                row_check[r][num] = col_check[c][num] = block_check[r // 3][c // 3][num] = True

    dfs(0)
#     print(matrix)
#
# solve_sudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#               [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#               ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#               [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#               [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
