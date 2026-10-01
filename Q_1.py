# Q1. Grocery bill calculator (~10 min)
# Write calculate_bill(**items) where each keyword argument is item=price.
# Return the total bill, 
# but apply a 10% discount if total exceeds 500.

# 1. Set total = 0.
# 2. Repeat for each item, price in items.items():
#    a. Add price to total.
# 3. Check: is total > 500?
#    - If yes, reduce total by 10%.
# 4. Return the final total.

def calculate_bill(**items):
    total = 0 
    for item , price in items.items():
        total += price
        
    if total > 500:
        total = total * 0.9
        
    return total

print(calculate_bill(rice = 200, sugar = 150, milk = 100, bread = 120, egg = 60))
    