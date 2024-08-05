def check_password_strength(password):
    '''
    Program to check the strength of input password
    Parameter:
    password (str): input password
    Returns:
    str: 'Weak' or 'Average' or 'Strong'
    '''

    special_chars = list("!@#$%&*")
    isdigit_there = any(char.isdigit() for char in password)
    islower_there = any(char.islower() for char in password)
    isupper_there = any(char.isupper() for char in password)
    special_char_there = any(char in special_chars for char in password)

    all_true = all([isdigit_there, isupper_there, special_char_there, islower_there])

    if len(password) < 6:
        return "Weak"
    elif len(password) >= 8 and all_true:
        return "Strong"
    else:
        return "Average"

input_password = input("Create Password: ")
strength = check_password_strength(input_password)
print("")
print("Your password is {} !!".format(strength))
