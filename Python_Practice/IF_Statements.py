def login():
    with open('users.txt', 'r') as file:
        login_info = file.readlines()
    user_dict = {}
    for pair in login_info:
        pair = pair.strip().split(':')
        user_dict[pair[0]] = pair[1]
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if username in user_dict and password == user_dict[username]:
        print("Success! You are now logged in.")
    else:
        print("Invalid login credentials. Please try again.")
login()