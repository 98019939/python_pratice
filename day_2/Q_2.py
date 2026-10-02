# Q2. Employee bonus calculator (~12 min)
# Write calculate_bonuses(employees) where employees is a dict of {name: years_worked}. Return a dict of {name: bonus} — bonus is ₹1000 per year, but capped at ₹10000.

# 1. Create an empty dict called bonuses.
# 2. Repeat for each name, years in employees.items():
#    a. bonus = years * 1000.
#    b. Check: is bonus > 10000?
#       - If yes, set bonus = 10000.
#    c. Add name: bonus to bonuses.
# 3. Return bonuses.
# 4. Loop through and print "Name: ₹bonus".


def calculate_bonuses(employees):
    bonuses = {}
    
    for name , year in employees.items():
        bonus = year * 1000
        
        if bonus > 10000:
            bonus = 10000
            
        bonuses[name] = bonus
        
    return bonuses

employees = {"Amit": 3, "Priya": 12, "Rahul": 7}
print(calculate_bonuses(employees))