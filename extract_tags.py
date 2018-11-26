def extract_tags(s):
    # assume that tags are properly matched
    a = []
    cache_left = []
    for i in range(len(s)):
        if s[i] == '[':
            cache_left.append(i)
        elif s[i] == ']':
            a.append(s[cache_left.pop() + 1: i])
    return a

print(extract_tags('[fizz] thing [/fizz] fuzz [zip]'))
print(extract_tags('[+ [1 2] ]'))

