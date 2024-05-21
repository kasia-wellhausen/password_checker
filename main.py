import string
import getpass

def check_pwd():
    password = getpass.getpass("Please enter your password: ")
    strength = 0
    remarks = '' #informs the user about the strength of the passoword
    lower_count = upper_count = num_count = whitespace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count +=1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            whitespace_count += 1
        else:
            special_count += 1

#check for strength of password based on the number of lower_count, upper_count, num_count, whitespace_count and special_count characters

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if whitespace_count >= 1:
        strength +=1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remarks = "Very poor strength, please update your password ASAP."
    elif strength == 2:
        remarks = "Not a good password. Change ASAP."
    elif strength == 3:
        remarks = "Your passowrd is weak. Please improve the strength."
    elif strength == 4:
        remarks = "Your passowrd is good but it can be better! Update it if you want to improve the strength."
    elif strength == 5:
        remarks = "This is very strong password. Well done!"

    print("Your password has: ")
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{whitespace_count} whitespace characters")
    print(f"{special_count} special characters")

    print(f"Your passowrd strength: {strength}")
    print(f"Hint: {remarks}")

#another function to recheck a new pasword after a weak password input
def recheck_pass(new_pass=False):
    valid = False
    if new_pass:
        choice=input("Would you like to input another password? (y/n):")
    else:
        choice=input("Would you like check password? (y/n):")

    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print("Invalid input. Please try again.")


if __name__ == '__main__':
    print('+++ Welcome to the password checker +++')
    recheck = recheck_pass()
    while recheck:
        check_pwd()
        recheck = recheck_pass(True)
