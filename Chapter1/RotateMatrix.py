# Time Complexity O(n.m)
# Space complexity Complexity O(1)
def rotateMatrix(matrix):
    # Transpose the Matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            # Switch the row and column indices
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':

    Input = [
        [1, 1, 1, 1],
        [2, 4, 8, 0],
        [3, 3, 6, 7],
        [5, 4, 2, 6]
        ]
    rotateMatrix(Input)

    for i in range(len(Input)):
        for j in range(len(Input)):
            # Switch the row and column indices
            print(Input[i][j],end='')
        print()

    for r in range(len(Input)):
        for i in range(len(Input[r]) // 2):
            oppI = len(Input[r]) - 1 - i
            Input[r][i], Input[r][oppI] = Input[r][oppI], Input[r][i]

    print()
    print()
    print()
    for i in range(len(Input)):
        for j in range(len(Input)):
            # Switch the row and column indices
            print(Input[i][j], end='')
        print()

    print()
    print(len(Input))