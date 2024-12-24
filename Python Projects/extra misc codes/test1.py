"""
generate random pw , contains
1.Uppercase alphabet
2.Lowercase alphabet
3.Digits
4.Special char
"""
def generate_pw(digits = 1, lowercase= 1, uppercase=1,symbol = 1):

    import re
    import secrets
    import string

    #print (dir(re))

    password = ""
    alphabet = string.ascii_letters
    digit = string.digits
    punctuation= string.punctuation

    all_char = alphabet + digit + punctuation


    while True:
        for i in range (16):
            password += secrets.choice(all_char)

        constraints = [(digits , r'[0-9]'),
                       (lowercase, r'[a-z]'),
                       (uppercase, r'[A-Z]'),
                       (symbol,fr'[{punctuation}]'),
                       ]


        if all(
            constraint <= len(re.findall(pattern,password))
            for constraint,pattern in constraints
        ):
            break

    return password
                   
                
password = generate_pw()
print(password)
