""" HackerRank practice problem for Python lists.

Task: You have to initialize your list L = [] and follow the N commands given in N lines. Commands will be 1 of the 8 commands as given above, other than extend, and each command will have its value separated by space."""

input_file = open("input.txt")

input_data = input_file.read().split("\n")

# N is number of commands in the input
N = int(input_data[0].strip())

L = []

# L = []

# N = int(raw_input().strip())

# for i in range(N + 1):
#     line = raw_input().strip().split()
#     if line[0] == "insert":
#         L.insert(int(line[1]), int(line[2]))
#     elif line[0] == "print":
#         print L
#         L = []
#     elif line[0] == "remove":
#         L.remove(int(line[1])
#     elif line[0] == "append":
#         L.append(int(line[1]))
#     elif line[0] == "sort":
#         L.sort()
#     elif line[0] == "pop":
#         L.pop()
#     else:
#         L.reverse()