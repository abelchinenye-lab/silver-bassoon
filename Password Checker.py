## Insert Password
password = input("Enter your password:")

## Create The Checks
has_upper = False
has_lower = False
has_digit = False
has_special = False

## Check Each Character
for character in password:
    if character.isupper():
        has_upper = True
    elif character.islower():
        has_lower = True
    elif character.isdigit():
        has_digit = True
    else:
        has_special = True

## Check Password Length
score = 0
if len(password) < 8:
    print("Password must be at least 8 characters long.")
    score += 1

## Check Conditions
if has_upper:
    score += 1

if has_lower:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

## Determine The Password Strength
if score == 5:
    strength = "Strong"
elif score >= 3:
    strength = "Medium"
else:
    strength = "Weak"

## Display Result
print("\nPassword Strength:", strength)
print("Score:", score, "/5")


