import random

def even_squares(nums):
    # return a list of squares of the even numbers in nums
    return [e ** 2 for e in nums if e % 2 == 0]

# test even squares
sequence = list(range(10))
# randomize
def swap(a, p, q):
    # helper function for randomizing
    temp = a[p]
    a[p] = a[q] 
    a[q] = temp

def randomize(a):
    for i in range(1, len(a)):
        r = random.randint(0, i)
        swap(a, r, i)

randomize(sequence)
print(sequence)
print(even_squares(sequence))

def sum_abs_product(a1, a2):
    # sum of the abs of the cross product between two list
    return sum([abs(e * f) for e in a1 for f in a2])

# (3 + 4) (3 + 4) = 49
print(sum_abs_product([3, 4], [3, -4]))
