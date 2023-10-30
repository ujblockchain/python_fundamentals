# one-parameter function
def introduction(user_name):
    print("Sawubona", user_name)

# two parameter function
def intro(user_name, email_address):
    print("Sawubona", user_name)
    print("Your email address is ", email_address)

# three-parameter function
def user_info(user_name, email_address, user_age):
    print("Sawubona", user_name,"!")
    print("Your email address is ", email_address)
    # conditional- check
    if int(user_age) >= 18:
        print(f"Welcome {user_name}, we will be sending you an account confirmation email.")
    else:
        print(f"Hi {user_name}, unfortunately you are too young to join our platform.")

# invoke the functions 
introduction("Bongi")

intro("Bongi", "bongi@mail.za")

user_info("Bongi", "bongi@mail.za",25)