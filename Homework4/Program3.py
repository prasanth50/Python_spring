num1 = [2,7,11,15]
target1 = 9


def find(x,y):
    index_map = {}
    for index, num in enumerate(x):
        if y-num in index_map:
            return index_map[y - num], index
        index_map[num] = index

print(find(num1,target1))
