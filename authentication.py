
# This the data base function
def data_base(first_name, last_name, email, password):
    global count_id
    data[f'id{count_id}'] = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password
        }
    count_id += 1

#This is a function to validate the users password
def validate_password(pass1, pass2):
    if pass1 == pass2:
        return pass1
    else:
        print("Wrong password match")
        sign_up()

#This is a function to sign up a new user
def sign_up():
    print("Sign Up")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email: ")
    pass1 = input("Enter Password: ")
    pass2 = input("Confirm Password: ")
    validated_password = validate_password(pass1, pass2)
    data_base(first_name, last_name, email, validated_password)
    print("You have successfully sign up")
    login()

# This is a function to login a user
def login():
    print("Log In")
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    for key, value in data.items():
        if email == value["email"] and password == value['password']:
            print("Log in successful")
            break
        if email != value["email"]:
            print("Wrong Email")
        elif password != value['password']:
            print("Wrong Password.")
        else:
            print("Create an account")
            menu()
    else:
        print("You don't have an account")
        sign_up()

"""
This is the main menu function that the user sees first
This function display the welcoming message and asks the
user if the want to login or sign up first
"""
def menu():
    print("Ojay Stores")
    print("Authentication Page")
    print("Type 1 to Login \nType 2 to Sign Up")

    user_option = input("Enter Option: ")

    if user_option == '1':
        login()
    elif user_option == "2":
        sign_up()
    else:
        print("You dont know how to read?")
        exit()


"""
This if name equals to main block restricts our program from
printing out some commands in another file if imported
"""
if __name__=='__main__':
    count_id = 1
    data = {}
    menu()