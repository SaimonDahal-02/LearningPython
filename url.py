import validators 
give_url = input("Enter url:") #
is_valid = validators.url(give_url)
if(is_valid):
    print("Given url is valid.")
else:
    print("Given url is not valid.")
