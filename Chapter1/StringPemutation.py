# Time Complexity O(n)
# Space complexity Complexity O(n)
def StringPermutation(string1, string2):
    list = [0] * 128
    for char in string1:
        list[ord(char)] += 1
    for char in string2:
        list[ord(char)] -= 1
        if list[ord(char)] == -1:
            return "Not permutation"
    return "Permutation"

if __name__ == '__main__':
    print(StringPermutation('helii', 'elhi'))