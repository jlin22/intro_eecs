def substring(s, t):
    # does there exist a substring
    # lets do string matching
    for i in range(len(t) - len(s)):
        if s == t[i: i + len(s)]:
            return True
    return False

print(substring('hello', 'hello world'))
print(substring('hello', 'world goodbye'))

# let's try to implement the rolling hash class to make a faster substring matchers
class RollingHash:
    x = ''
    h = 0
    def add(self, c):
        self.x += c
        self.h *= 256 
        self.h += ord(c)
        
    def delete(self, c):
        self.x = self.x[1:]
        self.h -= ord(c) * 256 ** (len(self.x) - 1) 

    def hash(self):
        return self.h

def karp_rabin(s, t):
    # substring with a more efficient algorithm
    rs, rt = RollingHash(), RollingHash()
    for e in s: rs.add(e)
    for i in range(len(s)): rt.add(t[i])
    if rs.hash() == rt.hash():
        if s == t[: len(s)]:
            return True
    for i in range(len(s), len(t)):
        rt.add(t[i])
        rt.delete(t[i - len(s)])
        if rs.hash() == rt.hash():
            if s == t[i - len(s): i]:
                return True
    return False

print(karp_rabin('hello', 'hello world!'))
print(karp_rabin('rdi', 'xordinate'))
print(karp_rabin('jam', 'jello'))


