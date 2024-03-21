'''
  Password validator that contains the following constraints:
  
   - Length between 12 and 20 characters 
   - At least three UpperCase Letters
   - At least three LowerCase letters
   - At least one digit
   - At least three special special characters
   - Only letters, numbers, and special characters ae allowed
   - Should not contain 5 same characters or numbers consecutively
   - Should not contain the username
   - Should not have 3 same special characters consecutively
   - Special characters should  be " !, @, $, #, &, %, ^, *, (,), _ , - and ~ " 
   
'''

def login_user():
    username = input("---> Enter Username: ")
    return username

def user_password():
    print("---> Password Must Contain ")
    print(" - Length between 12 and 20 characters ") 
    print(" - At least three UpperCase Letters ")
    print(" - At least three LowerCase letters ")
    print(" - At least one digit ")
    print(" - At least three special special characters ")
    print(" - Only letters, numbers, and special characters ae allowed ")
    print(" - Should not contain 5 same characters or numbers consecutively ")
    print(" - Should not contain the username ")
    print(" - Should not have 3 same special characters consecutively ")
    print(" - Special characters should  be  !, @, $, #, &, %, ^, *, (,), _ , - and ~ ") 

def pass_length_validator(password):
    minimum = 12
    maximum = 20
    if len(password) < minimum or len(password) > maximum:
        return False
    return True

def uppercase_validator(password):
    ucase_count = password.count(char for char in password if char.isupper())
    if ucase_count < 3:
        return False
    return True

def lowercase_validator(password):
    lcase_count = password.count(char for char in password if char.islower())
    if lcase_count < 3:
        return False
    return True

def digit_check(password):
    if any(password.isdigit()):
        return True
    return False

def special_character_check(password):
    return password.count("!@#$%^&*()_-~") >= 3
