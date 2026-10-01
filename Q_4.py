# Q4. Retry-limited login (recursion-free, real scenario) (~12 min)
# Write login_attempt(correct_password) that gives the user 3 tries using a loop (not infinite), using break on success and a counter for attempts.

# 1. Set attempts = 0.
# 2. Repeat while attempts < 3:
#    a. Ask for password input.
#    b. Check: does it match correct_password?
#       - If yes, print "Login successful" and break.
#       - If no, add 1 to attempts, print "Wrong password, tries left: X".
# 3. If loop ends without success (attempts hit 3), print "Account locked".

def login_attempt(correct_password):
    attempts = 0

    while attempts < 3:
        password = input("Enter password: ")

        if password == correct_password:
            print("Login successful")
            break
        else:
            attempts += 1
            print("Wrong password, tries left:", 3 - attempts)

    if attempts == 3:
        print("Account locked")


# Correct password
correct_password = "python123"

# Start login
login_attempt(correct_password)