"""
head
 v
(X) -> (Z) -> (A) -> (B) -> (C) -> None

"""
# All you need really to keep track of - pointer and head
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
# some times nice to wrap in ll class

class LinkedList:
    # head
    #   v
    # None
    # next step result
    # head
    #  v
    # (11) -> None
    #  ^
    # cur
    def __init__(self):
        self.head = None

    def insert_at_head(self, node):
        # set pointer to next node
        node.next = self.head
        # set pointer to new head
        self.head = node
        
    def find(self, value):
        cur = self.head
        # walk through linked list
        while cur is not None:
            if cur.value == value:
                # found it
                return cur
            # keep looking/ moving pointer 
            cur = cur.next
        # if not found
        return None

    def delete(self, value):
        cur = self.head

        # Special case of deleting the head of the list
        #          head
        #           v
        # (11) -> (15) -> None
        #  ^
        # cur
        if cur.value == value:
            self.head = self.head.next
            return cur
        # General case just node in list
        # head
        #   v              DEL
        # (11) -> (15) -> (18) -> (20) -> None
        #           ^       ^
        #          prev    cur
        prev = cur
        cur = cur.next
        # walk both pointers along list
        while cur is not None:
            if cur.value == value: # Delete this one
                prev.next = cur.next # Cuts out the old node
                return cur
                
            else:
                prev = prev.next
                cur = cur.next
        return None

if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_head(Node(11))
