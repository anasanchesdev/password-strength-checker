length = False
uppercase = False
digit = False
results = []
points = 0

while True:
    password = input('Enter a new password:\n > ')

    if not any(password):
        print("You must type at least one character.")
        continue

    if len(password) >= 8:
        length = True

    for char in password:
        results = [length, uppercase, digit]
        if char.isupper() and not uppercase:
            uppercase = True
        elif char.isdigit() and not digit:
            digit = True

    for item in results:
        if item:
            points += 1

    if points == 3:
        print('Strong password.')
    elif points == 2:
        print('Moderated password.')
    elif points <= 1:
        print('Weak password.')
