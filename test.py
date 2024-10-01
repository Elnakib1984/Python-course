'''
usernames = []

def userInput():
  global usernames
  print("Welcome to this testing file\n")
  username = input("Please type your name:")

  usernames.append(username)


userInput()
print("listed usernames are", usernames)

'''

usernames = []

def userInput():
    while True:
        print("Welcome to this testing file\n")
        username = input("Please type your name (or type 'q' to quit): ")
        
        if username.lower() == 'q':  # Exit condition
            break
        
        usernames.append(username)  # Add the input to the list

    print("\nList of usernames entered:")
    for name in usernames:
        print(name)
        

userInput()


