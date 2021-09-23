# Time Complexity O(n)
# Space complexity Complexity O(1)
def oneAway(string1 , string2):
    count1 = 0
    count2 = 0
    check = False
    print(len(string1))
    print(len(string2))
    while count1 < len(string1) and count2 < len(string2):

        if string1[count1] == string2[count2]:
            count1 += 1
            count2 += 1
        elif not check:
            check = True
            if len(string1) == len(string2):
                count1 += 1
                count2 += 1
            elif len(string1) < len(string2):
                count2 += 1
            elif len(string1) > len(string2):
                count1 += 1
        else:
            return False
    return True


if __name__ == '__main__':
    print(oneAway('ali', 'all'))