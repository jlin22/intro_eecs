def palindrome(s):
    # is s a palindrome (excluding strings)

    # double pointer method
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        # update pointers
        i, j = i + 1, j - 1
        while s[i] == ' ':
            i += 1
        while s[j] == ' ': 
            j -= 1
    return True

# test palindrome
print(palindrome(''))
print(palindrome('alomomola'))
print(palindrome('able was I ere I saw elba'))
print(palindrome('a man a plan a canal panama'))
print(palindrome('cat'))
