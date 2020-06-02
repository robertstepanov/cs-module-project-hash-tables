['Lorem', 'ipsum', 'dolar', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']
0 1 2 3 4 5 6 7

'amet' => [magic box] -> 4
'amet' => [magic box] -> 4
'amet' => [magic box] -> 4
'amet' => [magic box] -> 4
'ipsum' => [magic box] -> 1

data = [None, None, None, None, None, None, None, None]

'bob' -> hashing_function() -> some index
'missi' -> hashing_function() -> some index

## Hash Table Load

0 |-> D Load factor: 3 / 8 = 0.3755
1 |->
2 |-> A
3 |-> C
4 |->
5 |->
6 |->
7 |->

0 |-> D Load factor: 8 / 8 = 1.0
1 |-> H
2 |-> A
3 |-> C
4 |-> G
5 |-> B
6 |-> E
7 |-> F

anything < 1 is underloaded over 1 is overloaded

0 |-> D -> M Load Factor: 16 / 2 = 2.0
1 |-> H
2 |-> A -> I
3 |-> C -> J -> L -> N
4 |-> G
5 |-> B -> O
6 |-> E - K -> P
7 |-> F

0 |-> D -> M - Q Load Factor 29 / 8 = 3.625
1 |-> H -> R - X -> Y
2 |-> A -> I
3 |-> C -> J -> L -> N - Z
4 |-> G -> S -> U
5 |-> B -> O -> 1 -> 2
6 |-> E - K -> P -> W
7 |-> F - T - V

## Load Factor

number of things stored in the hash table / number of slots in the array

When computing the load, keep track of the number of items in the hash table as you go.

- When you put a new item in the hash table, increment the count
- When you delete an item from the hash table, decrement the count

When is the hash table overloaded?

- It's overloaded when load factor > 0.7
- It's underloaded when load factor < 0.1 (Stretch)

## Resize the Hash Table

Resize:

1. Allocate a new array of bigger size, typically double the previous size (or half the size if resizing down, down to some minimum)
2. Traverse the old hash table -- O(n) over the number of elements in the hash table
   For each of the elements:
   Figure out its slot in the bigger (or smaller), new array
   Put it there
