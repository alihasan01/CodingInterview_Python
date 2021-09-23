# Time Complexity O(n)
# Space complexity Complexity O(n)
def StringCompression(str2):
    compressedString = []
    current = str2[0]
    counter = 1
    for itr in str2[1:]:
        if itr == current:
            counter += 1
        else:
            compressedString.append(current)
            compressedString.append(str(counter))
            counter = 1
            current = itr

    compressedString.append(current)
    compressedString.append(str(counter))
    compressedString = "".join(compressedString)

    if len(compressedString) < len(str2):
       return str2
    else:
       return compressedString


if __name__ == '__main__':
    print(StringCompression('afw'))