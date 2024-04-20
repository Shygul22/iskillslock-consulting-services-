username = input("ENTER YOUR USERNAME")
password = input("ENTER YOUR PASSWORD")

user = "akbar"
passwrd = "shygul"

def login():
    global user, password
    if (user == username and passwrd == password):
        print ("LOGIN SUCCESSFUL")
    else:
        print ("USERNAME OR PASSWORD INCORRECT")

login()