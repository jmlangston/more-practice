"""Practice with tuples from HackerRank.

Should return 3713081631934410656 """

input_str = '1 2'

values = input_str.split()

# list comprehension to call int() on each item in list
values = [int(x) for x in values]

T = tuple(values)

print hash(T)
