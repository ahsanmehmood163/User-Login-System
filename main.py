granted = False
name = ""  # Initialize name as an empty string

def grant():
    global granted
    granted = True

def login(name, password):
    success = False
    with open("user_detail.txt", "r") as file:  # Use 'with' statement for file handling
        for line in file:
            a, b = line.strip().split(",")
            if a == name and b == password:
                success = True
                break
    if success:
        print("Login Successful")
        grant()
    else:
        print("Wrong username or password")

def register(name, password):
    with open("user_detail.txt", "a") as file:
        file.write("\n" + name + "," + password)
    grant()

def access(option):
    global name
    if option == "login":
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        login(name, password)
    else:
        print("Enter your name and password to register")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        register(name, password)

def begin():
    global option
    print("Welcome to Victor's programming club")
    option = input("Login or Register (login, reg): ").lower()  # Convert input to lowercase
    if option not in ["login", "reg"]:  # Check if the input is valid
        print("Invalid option. Please enter 'login' or 'reg'")
        begin()

begin()
access(begin())

if granted:
    print("Welcome to Victor's Programming club")
    print("### USER DETAILS ###")
    print("Username: ", name)
