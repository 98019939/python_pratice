# Q1. Electricity bill calculator (~10 min)
# Write electricity_bill(units) that returns the cost based on slabs: first 100 units free, next 100 units at ₹5/unit, anything above 200 at ₹8/unit.

# 1. Set bill = 0.
# 2. Check: is units <= 100?
#    - If yes, bill = 0.
# 3. Else check: is units <= 200?
#    - If yes, bill = (units - 100) * 5.
# 4. Else:
#    - bill = (100 * 5) + (units - 200) * 8.
# 5. Return bill. Call it with units = 50, 150, 300 and check each result.

def electricity_bill(units):
    bill = 0
    if units <= 100:
        bill = 0
        
    elif units <= 200:
        bill = (units - 100)*5
        
    else:
         bill = (100 *5)+ (units - 200)* 8
        
    return bill


print(electricity_bill(50))