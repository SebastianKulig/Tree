import math


class Node:

    def __init__(self, data, lvl):
        self.left = None
        self.right = None
        self.data = data
        self.lvl = lvl

    def insert_from_left_to_right(self, data):
        if self.data is not None:

            if self.left is None:
                self.left = Node(data, self.lvl + 1)
            elif self.right is None:
                self.right = Node(data, self.lvl + 1)
            else:
                self.left.insert_from_left_to_right(data)
        else:
            self.data = data

    def insert_from_right_to_left(self, data):
        if self.data is not None:
            if self.right is None:
                self.right = Node(data, self.lvl + 1)
            elif self.left is None:
                self.left = Node(data, self.lvl + 1)
            else:
                self.right.insert_from_right_to_left(data)
        else:
            self.data = data

    def print_lvl(self):
        if self.lvl == 1:
            print("-", self.data, "LEVEL: ", self.lvl)
        if self.left:
            for i in range(self.lvl):
                print("     ", end="")
            print("-", self.left.data, "LEVEL: ", self.lvl + 1)
            self.left.print_lvl()

        if self.right:
            for i in range(self.lvl):
                print("     ", end="")
            print("-", self.right.data, "LEVEL: ", self.lvl + 1)
            self.right.print_lvl()


# ===================================================================================================================================================================================
def create_tree():
    # Create a tree
    values_l = [3, 7, 2, 5]
    root = Node(5, 1)
    for v in values_l:
        root.insert_from_left_to_right(v)

    values_r = [0, 1, 8, 2, 5]
    for v in values_r:
        root.right.insert_from_right_to_left(v)
    return root


# finding node with right values
def search(value, level):
    visited_nodes(root_of_tree)
    for l in list_of_visited_leafs:
        if l.data == value and l.lvl == level:
            list_of_visited_leafs.clear()
            return l
    return None



# sum data of all nodes beneath node
def sum_data(node):
    if node is None:
        return 0
    return node.data + sum_data(node.left) + sum_data(node.right)


def sum_data_in_tree(start, tier):
    return sum_data(search(start, tier))


def mean(start, tier):
    visited_nodes(search(start, tier))
    length = len(list_of_visited_leafs)
    list_of_visited_leafs.clear()
    return sum_data_in_tree(start, tier) / length


list_of_visited_leafs = []


# create list of all nodes beneath start_point
def visited_nodes(start_point):
    if start_point is None:
        return None
    list_of_visited_leafs.append(start_point)
    if start_point.left is not None:
        visited_nodes(start_point.left)
    if start_point.right is not None:
        visited_nodes(start_point.right)


def take_data(elem):
    return elem.data


# sort list of nodes and choose median
def median(start, tier):
    visited_nodes(search(start, tier))

    list_of_visited_leafs.sort(key=take_data)
    length = len(list_of_visited_leafs)

    if length % 2 != 0:
        tmp = list_of_visited_leafs[math.ceil(length / 2) - 1].data
        list_of_visited_leafs.clear()
        return tmp
    else:
        value1 = list_of_visited_leafs[int((length / 2) - 1)].data
        value2 = list_of_visited_leafs[int((length / 2))].data
        list_of_visited_leafs.clear()
        return (value1 + value2) / 2


# ===============================================================================================================================================================================
# create tree
nodes = [5, 3, 7, 2, 0, 1, 8]
root_of_tree = create_tree()
root_of_tree.print_lvl()

# User input

print("Od ktorego elementu zacząć sumować: ")

while True:
    try:
        start = int(input())
    except ValueError:
        print("Nie ma takiego elementu, spróbuj jeszcze raz: ")
        continue
    else:

        if start in nodes:
            break
        else:
            print("Nie ma takiego elementu, spróbuj jeszcze raz: ")
            continue

print("Na którym poziomie, licząc od góry, znajduje się wybrana wartość początkowa: ")

while True:
    try:
        tier = int(input())
    except ValueError:
        print("Nie ma takiej wartości na tym poziomie, spróbuj jeszcze raz: ")
        continue
    else:

        if search(start, tier) is not None:
            break
        else:
            print("Nie ma takiej wartości na tym poziomie, spróbuj jeszcze raz: ")
            continue

# Operations

print("Suma: ")
print(sum_data_in_tree(start, tier))

print("Średnia: ")
print(mean(start, tier))

print("Mediana")
print(median(start, tier))
