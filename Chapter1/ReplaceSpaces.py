def ReplaceSpaces(string1):
    stringLength = len(string1)
    count = 0
    for char in string1:
        if char == ' ':
            count += 1
    newLength = stringLength + (count * 2)
    print(newLength)
    print(stringLength)
    list = [0] * newLength
    i = 0
    acc = 0
    print(string1)
    while i < len(string1) - 1:
        print(acc)
        if char == ' ':
            list.append('%')

            list.append('2')

            list.append('1')
            acc = acc + 1
            i += 2
        else:
            list.append(string1[acc])
            acc = acc + 1
            i += 1
    print  (list)


if __name__ == '__main__':
    print(ReplaceSpaces('ali ha'))