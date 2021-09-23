# Time Complexity O(n)
# Space complexity Complexity O(n)
def insUnique (str):
    myList = [0] * 128
    for char in str:
        chint = ord(char)
        if myList[chint]:
            return "Not unique"
        myList[chint] = True
    return "Unique"
if __name__ == '__main__':
    print(insUnique('heli'))