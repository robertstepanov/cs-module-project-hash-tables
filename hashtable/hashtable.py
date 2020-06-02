class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'HashtableEntry({repr(self.key)},{repr(self.value)})'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.table = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here

        return len(self.table)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here

        # number of things stored in the hash table / number of slots in the array
        # When computing the load, keep track of the number of items in the hash table as you go.
        # - When you put a new item in the hash table, increment the count
        # - When you delete an item from the hash table, decrement the count
        pass

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        pass
        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        self.table[i] = HashTableEntry(key, value)

        # # Day 2 refactor
        # Find slot for the key
        # i = self.hash_index(key)

        # # Search Ll for the key
        # newHashTableEntry = HashTableEntry(key, value)

        # If found, update it
        # if self.table[i] is not None:
        #     newHashTableEntry.next = self.table[i]

        # If not found, make a new HashTableEntry and add it
        # self.table[i] = newHashTableEntry

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)

        if self.table[i] == None:
            print('No key found')
        else:6
            self.table[i] = None

        # Day 2 refactor

        # Find the slot for the key
        # Search LL for the key
        # If found, delete it from LL and reassign pointers
        # If not found return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        i = self.hash_index(key)

        if self.table[i] == None:
            return None
        else:
            return self.table[i].value

        # # Day 2 refactor

        # # Find the slot for the key
        # i = self.hash_index(key)
        # value = None

        # # Search the LL for the key
        # If found return value

        # if self.table[i] is not None:
        #     node = self.table[i]

            # If not found keep looking
        #     while node is not None and value is None:
        #
        #         if node.key == key:
        #             value = node.value
        #         else:
        #             node = node.next
        # return value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # 1. Allocate a new array of bigger size, typically double the previous size (or half the size if resizing down, down to some minimum)
        # 2. Traverse the old hash table -- O(n) over the number of elements in the hash table
        #     For each of the elements:
        #     Figure out its slot in the bigger (or smaller), new array
        #     Put it there


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
