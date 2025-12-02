from collections import Counter, OrderedDict

list = ['B','B','A','B','C','A','B','B','A','C']


# 1. Counter
print(Counter(list))
# output - Counter({'B': 5, 'A': 3, 'C': 2})

# 2 OrderDict - Order maintains - dict also but only version 3.7+

# normal Dictionary
d = {}
d["a"] = 1
d["b"] = 2
d["c"] = 3
d["d"] = 4

print(f'normal dictionary: {d}')

# orderDict
od = OrderedDict()

od["a"] = 1
od["b"] = 2
od["c"] = 3
od["d"] = 4

print(f'ordered dictionary: {od}')

# now the difference comes to the picture 
# - in this eg we delete in key and value and insert the same k,v again it inserts last in the dictionary

od.pop("a")

od["a"] = 1

print(f'after delete amd insert the same element: {od}')


