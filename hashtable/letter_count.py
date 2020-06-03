
def print_letter_count(s):
    counts = {}

    for c in s:
        #c = c.lower() # case sensitive
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    items = list(counts.items())
    items.sort(key=lambda e: e[1], reverse=True)

    print(items)



print_letter_count('aaaabbcbcaAAB!👍')