# Time Complexity O(n.m)
# Space complexity Complexity O(1)
def zeroMatrix(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                setNone(matrix, r, c)

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == None:
                matrix[r][c] = 0

def setNone(matrix, r, c):
    # set the row to None
    for i in range(len(matrix[r])):
        if matrix[r][i] != 0:
            matrix[r][i] = None

    # set the column to None
    for i in range(len(matrix)):
        if matrix[i][c] != 0:
            matrix[i][c] = None

    matrix[r][c] = None

if __name__ == '__main__':

    Input = [
        [1, 1, 1, 1],
        [2, 4, 8, 0],
        [3, 3, 6, 7],
        [5, 0, 2, 6]
        ]
    zeroMatrix(Input)

    for i in range(len(Input)):
        for j in range(len(Input)):
            # Switch the row and column indices
            print(Input[i][j], end='')
        print()
