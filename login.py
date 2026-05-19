db = {}


def signup():
    username = input("Enter User Name: ")
    password = input("Enter Password: ")
    if username not in db:
        db[username] = password
        print(username, password)
    return "Signup Successful!"


print(signup())

print(db)


def login():
    username = input("Enter User Name: ")
    password = input("Enter Password: ")

    if username in db and db[username] == password:
        print(username, password)
        return "Login Successful!"
    else:
        return "Wrong Credentials. Try Again With Correct Credentials."


print(login())
