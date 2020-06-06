l = [10, 12, 1, 4, 7, 11]

# filter function using lambda function
fl = list(filter(lambda num: num > 7, l))
print(fl)

# output
# [10, 12, 11]

# map function using lambda function
ml = map(lambda num: num+1, l)
print(type(ml))
print(list(ml))

# output
# <class 'map'>
# [11, 13, 2, 5, 8, 12]
