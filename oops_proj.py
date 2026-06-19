class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook !! How would you like to proceed?
        1. Press 1 to signup
        2. Press 2 to signin
        3. Press 3 to write a post
        4. Press 4 to message a friend
        5. Press any other key to exit""")

        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()

    def signup(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        print("Signup successful !!")
        self.menu()
    def signin(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == self.username and password == self.password:
            self.loggedin = True
            print("Signin successful !!")
        else:
            print("Invalid username or password !!")
        
        self.menu()
    def write_post(self):   
        if self.loggedin:
            post = input("Write your post: ")
            print("Post successful !!")
        else:
            print("Please signin to write a post !!")
        self.menu()
    def message_friend(self):
        if self.loggedin:
            friend = input("Enter your friend's username: ")
            message = input("Enter your message: ")
            print("Message sent to " + friend + " !!")
        
        else:
            print("Please signin to message a friend !!")
        self.menu()
object = chatbook()