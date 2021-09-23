# Time Complexity O(n+m)
# Space complexity Complexity O(n+m)
def StringRotation(str1 , str2):
    str3 = str2 + str2
    if str1 in str3:
        return True
    else:
        return False

if __name__ == '__main__':
    print(StringRotation("CodingInterview", "erviewCodingInt"))
