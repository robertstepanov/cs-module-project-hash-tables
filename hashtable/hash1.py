# data = [None, None, None, None, None, None, None, None]
#same as above
data = [None] * 8

# def my_hashing_function(s):
    
    
#     for c in s:
#         print(c)

# my_hashing_function('bob')


# def my_hashing_function2(s):
#     string_bytes = s.encode()
#     for b in string_bytes:
#         print(b)

# my_hashing_function2('bob')

# ---------------------------------------------------------------------------

# if hash_entry is not None:
#     return print('not a valid entry')

# ---------------------------------------------------------------------------

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'HashTableEntry({repr(self.key)}, {repr(self.value)})'

def my_hashing_function_sum(s):
    string_bytes = s.encode()

    total = 0
    for b in string_bytes:
        total += b
    return total
        

# print(my_hashing_function_sum('total'))

def get_slot(s):
    hash_val = my_hashing_function_sum(s)
    return hash_val % len(data)

def get(key):
    slot = get_slot(key)
    return data[slot]

def put(key, value):
    slot = get_slot(key)
    data[slot] = value

def delete(key):
    put(key, None)

# print(get_slot('bob'))
# print(get_slot('missi'))
# print(get_slot('felix'))
# print(get_slot('leopold'))
# print(get_slot('max'))

put('bob', 'GOAT')
put('missi', 8800)

print(get('bob'))
print(get('missi'))
print(get('felix'))

print(data)
