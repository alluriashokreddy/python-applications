# zip function
lhead = ['first','middle','last']
lrow = ['ashok','reddy','alluri']

for t in zip(lhead,lrow):
    print(t)

# output:
# ('first', 'ashok')
# ('middle', 'reddy')
# ('last', 'alluri')


# map function
def addition(first, second):
    return first+second


l1 = [1, 2, 3, 4]
l2 = [4, 5, 6, 7]
for t in map(addition,l1, l2):
    print(t)

# output
# 5
# 7
# 9
# 11

# enumerate function
l = ['ashok', 'reddy', 'alluri']
for i in enumerate(l):
    print(i)
# output
# (0, 'ashok')
# (1, 'reddy')
# (2, 'alluri')


# filter function
def check(val):
    if val > 10:
        return True
    else:
        return False


l = [10, 12, 1, 4, 7, 11]
for i in filter(check, l):
    print(i)

# output
# 12
# 11

# min, max, sum functions
l = [10, 12, 1, 4, 7, 11]
print(min(l))
print(max(l))
print(sum(l))
print(len(l))
print(sorted(l))  # returns the sorted list, not in-line change,
print(l)

# output
# 1
# 12
# 45

# reversed function
l = [10, 12, 1, 4, 7, 11]
lr = reversed(l)
for i, j in zip(l, lr):
    print(i, j)

# output
# 10 11
# 12 7
# 1 4
# 4 1
# 7 12
# 11 10