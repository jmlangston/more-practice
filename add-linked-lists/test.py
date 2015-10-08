class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_rev_string(self):

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(reversed(out))


# def add_linked_lists(l1, l2):

l1 = Node(3, Node(2, Node(1)))
l2 = Node(6, Node(5, Node(4)))

num1 = l1.as_rev_string()
# print num1
num2 = l2.as_rev_string()
# print num2

num_sum = str(int(num1) + int(num2))
# print num_sum

# list_nums = list(num_sum).reverse()
list_nums.reverse()

# print list_nums

list_nodes = []

next_node = None

for num in list_nums:
    new_node = Node(num, next_node)
    list_nodes.append(new_node)
    next_node = new_node

print list_nodes[-1]
