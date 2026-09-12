
## Define Userrname and Password
users = {
     "Chichi":"Chichi123", "David":"Dave345", "Bola":"Bolaola456", "Ada": "Adada678", "Evelyn":"Evely789"
}

## User Input
username = input("Enter your username: ")
password = input("Enter your password: ")

## Check Login Credentials
if username in users:
    if password == users[username]:
        print("Login Successful!")
    else:
        print("Incorrect Password.")
else:
    print("Username not found.")