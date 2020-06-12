import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# OLD RUNTIME: n^2

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Binary tree 
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    def contains(self, target):
        node = self
        while node.value != target:
            if node.value < target:
                node = node.right
            else:
                node = node.left
            if node is None:
                return False
        return True    

# Initialize 
binary_tree = BSTNode("empty")

# Put all names_1 in to a binary tree
for name_1 in names_1:
    binary_tree.insert(name_1)
for name_2 in names_2:
    # Check names_1 for names_2 duplicates
    if binary_tree.contains(name_2):
        # Append duplicates
        duplicates.append(name_2)

# NEW RUNTIME:  nlogn

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
