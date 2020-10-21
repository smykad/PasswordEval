#   ******************************
#   Doug Smyka
#   Password Evaluation Application
#   Date Created: 10.19.2020
#   Date Revised: 10.20.2020
#   ******************************

import re
import pyinputplus as pyip

#   ******************************
#   METHODS
#   ******************************


#   ******************************
#   USER PASSWORD
#   ******************************
def user_password():
    # hides user input when they type in their password
    password = pyip.inputPassword("Password: ")
    return password


#   ******************************
#   PASSWORD IN ASTERISK
#   ******************************
def obfuscate(password):

    # obfuscates users password with asterisks

    obfuscated_password = '*' * len(password)

    # returns the obfuscated password

    return obfuscated_password


#   ******************************
#   PASSWORD VALIDATION
#   ******************************

# accepts the parameter password

def valid_password(password):

    # uses the method 'obfuscate' and passes along the parameter 'password' to it

    obfuscated_pw = obfuscate(password)

    password_len = len(password)
    # A loop to determine the validity of the password

    while True:

        #  Check length of password

        if password_len < 8:
            print(f"Your password [{obfuscated_pw}] is too short")
            break

        #  Check for lowercase letters in password

        elif not re.search("[a-z]", password):
            print(f"Your password [{obfuscated_pw}] does not contain lower case letter(s)")
            break

        #  Check for upper case letters in password

        elif not re.search('[A-Z]', password):
            print(f"Your password [{obfuscated_pw}] does not contain upper case letter(s)")
            break

        #  Check for numbers

        elif not re.search("\\d", password):
            print(f"Your password [{obfuscated_pw}] does not contain a number")
            break

        #  Checks for special characters listed

        elif not re.search("[,'\"!@#$%^&*()-=+_]", password):
            print(f"Your password [{obfuscated_pw}] does not contain special character")
            break

        #  Checks for white space

        elif re.search("\\s", password):
            print(f"Your password [{obfuscated_pw}] should not contains whitespace")
            break

        #  Made it through the loop, password checks out

        else:
            print(f"Your password [{obfuscated_pw}] is valid")
            break


#   ******************************
#   MAIN METHOD
#   ******************************

#  Gets users password
#  Validates or invalidates users password

def main():
    password = user_password()
    valid_password(password)
    input("Press any key to exit")


#   ******************************
#   MAIN
#   ******************************

main()

#  EOF

