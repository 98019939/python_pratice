# Q2. List + *args + continue (~10 min)
# Write stats(*args) that returns total, highest and lowest, ignoring negative numbers.

# 1. Set total = 0. Set highest and lowest = None (no value yet).
# 2. Repeat for each number in args:
#    a. If number < 0, skip it (continue).
#    b. Add it to total.
#    c. If highest is None or number > highest, update highest.
#    d. If lowest is None or number < lowest, update lowest.
# 3. Return total, highest, lowest.

def stat(*args):
    total = 0
    highest = None
    lowest = None
    
    for i in args:
        if i < 0:
            continue
        
        total += i
        
        if highest is None or i > highest:
            highest = i
        
        if lowest is None or i < lowest:
            lowest = i
        
    return total, highest, lowest

print(stat(5, -3, 4, 8, 12))
print(stat(-4, -8))
print(stat())