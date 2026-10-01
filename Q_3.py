# Write ticket_price(age, day="weekday")
# that returns the price based on rules: under 12 → 100, 12-60 → 200 (250 if day is "weekend"),
# above 60 → 150.

# 1. Check age range using if/elif/else.
# 2. Inside the 12-60 branch, check day — if "weekend", price is 250, else 200.
# 3. Return the final price.
# 4. Call it with a few different age + day combinations.

def ticket_price(age, day="weekday"):
    if age < 12:
        price = 60
        
    if age >= 12 and age < 60:
        price = 200
        
        if day == "weekday":
            
            price = 250
            
    else:
        price = 150
        
    return price

print(ticket_price(15, "weekday"))
print(ticket_price(63, "weekday"))