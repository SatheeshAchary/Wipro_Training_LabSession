""" Set: A set is a collection of:

1. Unique elements (no duplicates)
2. Unordered
3. No indexing """

#Empty set
s = set()

s = {10, 20, 30}

s.add(40)
print(s)

s.update([50, 60])
print(s)

s.remove(20)

s.discard(100)

s.pop()

s.clear()

#Set Operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))

print(a.intersection(b))

print(a.difference(b))

print(a.symmetric_difference(b))

#Set Comparison
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))

print(b.issuperset(a))

print(a.isdisjoint({4, 5}))

#Checking
print(10 in s)

#FrozenSet Means We cannot add or delete the elements
fs = frozenset([1, 2, 3])
