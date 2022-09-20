"""from validate_email import validate_email

#Importing valid_email syntax from library

email = input("Enter the email: ") #Taking the email

isValid = validate_email(email, verify = True) # bool value, True if email is valid

#checking if the email is valid.
if isValid:
    print("Email is valid.")
else:
    print("Email is not valid.")"""
import re
email = input("Enter email: ")
def validate_email(email):
    email_regx = re.compile('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if email_regx.match(email):
         return "Valid Email."
    else:
        return "Invalid Email."
print(validate_email(email = email))