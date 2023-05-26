
def data_base(first_name, last_name, email, password):
    global count_id
    data[f'id{count_id}'] = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password
        }
    count_id += 1

def validate_password(pass1, pass2):
    if pass1 == pass2:
        return pass1
    else:
        print("Wrong password match")
        sign_up()

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


if __name__=='__main__':
    count_id = 1
    data = {}
    menu()