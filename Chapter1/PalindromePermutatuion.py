# Time Complexity O(n)
# Space complexity Complexity O(n)
def PalindromPermutation(str):
    list = [0] * 26  # Creating array for holding 26 numeric values of characters\
    count = 0
    for char in str:
        c = int(char, 36)
        list[c] += 1
        if list[c] % 2 == 1:
            count += 1
        else:
            count -= 1
    if count <= 1:
        return True
    else:
        return False


if __name__ == '__main__':
    print(PalindromPermutation('adlliiiiaa'))
