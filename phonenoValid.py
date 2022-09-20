import phonenumbers
phonenumberstring = input("Enter the phone number with country code: ")
pnValid = phonenumbers.parse(phonenumberstring)
if (phonenumbers.is_possible_number(pnValid)):
    print("The phone number is valid.")
else:
    print("The phone number is not valid.")