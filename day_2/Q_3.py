# Q3. Password strength checker (~10 min)
# Write check_strength(password) that returns "Weak", "Medium", or "Strong" based on: length >= 8 AND has a digit AND has an uppercase letter → Strong; length >= 6 and meets 1-2 conditions → Medium; otherwise Weak.

# 1. Set has_digit = False, has_upper = False.
# 2. Repeat for each character in password:
#    a. Check: is it a digit? If yes, has_digit = True.
#    b. Check: is it uppercase? If yes, has_upper = True.
# 3. Count how many conditions are True (length >= 8, has_digit, has_upper).
# 4. Use if/elif/else on that count to decide Weak/Medium/Strong.
# 5. Return the result. Test with 3-4 different passwords.

def password_strength(password):
    
    has_digit = False
    has_upper = False
    
    for char in password:
        if char.isdigit():
            has_digit = True
            
        if char.isupper():
            has_upper = True
            
    score = 0
    
    if len(password) >= 8:
        score += 1
        
    if has_digit:
        score +=1
        
    if has_upper:
        score+=1
        
    if score == 3:
        return "Stronge"
    
    elif score == 2:
        return "medium"
    
    else:
        return "Weak"
    
passwords= [
    "Hello",
    "Hello1",
    "Hello123456"
]

for password in passwords:
    print(password, "-->", password_strength(password))