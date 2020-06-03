# Let's sort a dictionary/hash table ie. by keys or values

# First have to get items out before sorting

a = {'a':2, 'b':3}

print(a)

print(a.items())

print(list(a.items()))

print(sorted(list(a.items())))


d = {
    'foo': 12,
    'bar': 17,
    'qux': 2
}

items = list(d.items())

# sort ascending by key
items.sort()

print(items)

# sort descending by key
items.sort(reverse=True)

print(dict(items))

# sort ascending by value
# def get_key(e): # e is going to be the tuple
#     # return the thing that we want to sort by
#     return e[1]

# items.sort(key=get_key)

# same as above
items.sort(key=lambda e: e[1])

print(items)

