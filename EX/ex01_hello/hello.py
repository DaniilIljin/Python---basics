# # a = 0
# # while a != "stop":
# #       a = input("Input number to check: ")
# #       if a.isalpha():
# #             continue
# #       else:
# #             a = int(a)
# #             while a != 1:
# #                   if a % 2 == 0:
# #                         print(f" Because {a} is even")
# #                         a = a / 2
# #                         print(f"a / 2 = {a}")
# #                   else:
# #                         print(f" Because {a} is odd")
# #                         a = 3 * a + 1
# #                         print(f"a * 3 + 1 = {a}")
# #             print("1\n\n")
#
#
# def op():
#       kategoria = input("Kategoria: 1 - vegetables, 2 - fruits, 3 - berries: ")
#       if kategoria == 1:
#             product = input("What product: 1-a, 2-b, 3-c: ")
#             if product == 1:
#                   price = 5
#             elif product == 2:
#                   price = 3
#             elif product == 3:
#                   price = 4
#             else:
#                   print("FUCK yOU")
#                   raise Exception
#       elif kategoria == 2:
#             product = input("What product: 1-a, 2-b, 3-c: ")
#             if product == 1:
#                   price = 5
#             elif product == 2:
#                   price = 3
#             elif product == 3:
#                   price = 4
#             else:
#                   print("FUCK yOU")
#                   raise Exception
#       elif kategoria == 3:
#             product = input("What product: 1-a, 2-b, 3-c: ")
#             if product == 1:
#                   price = 5
#             elif product == 2:
#                   price = 3
#             elif product == 3:
#                   price = 4
#             else:
#                   print("FUCK yOU")
#                   raise Exception
#       else:
#             print("FUCK yOU")
#             raise Exception
#       print(price)

graph = [[1, 2], [1, 3], [1, 4], [2, 3], [3, 4], [2, 6], [4, 6], [8, 7], [8, 9], [9, 7]]
cycles = []

def main():
    global graph
    global cycles
    for edge in graph:
        for node in edge:
            findNewCycles([node])
    for cy in cycles:
        path = [str(node) for node in cy]
        s = ",".join(path)
        print(s)

def findNewCycles(path):
    start_node = path[0]
    next_node= None
    sub = []

    #visit each edge and each node of each edge
    for edge in graph:
        node1, node2 = edge
        if start_node in edge:
                if node1 == start_node:
                    next_node = node2
                else:
                    next_node = node1
                if not visited(next_node, path):
                        # neighbor node not on path yet
                        sub = [next_node]
                        sub.extend(path)
                        # explore extended path
                        findNewCycles(sub);
                elif len(path) > 2  and next_node == path[-1]:
                        # cycle found
                        p = rotate_to_smallest(path);
                        inv = invert(p)
                        if isNew(p) and isNew(inv):
                            cycles.append(p)

def invert(path):
    return rotate_to_smallest(path[::-1])

#  rotate cycle path such that it begins with the smallest node
def rotate_to_smallest(path):
    n = path.index(min(path))
    return path[n:]+path[:n]

def isNew(path):
    return not path in cycles

def visited(node, path):
    return node in path

main()