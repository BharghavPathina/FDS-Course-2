'''
This is main program

'''

# import sys
# sys.path.append("./")
from utils import (
    read_choice,
    user_menu
)

print("hello!")

def main():
    print("Welcome to the LMS..!")

    flag = True
    while flag:
        print("Select your type: \n1.USER\n2.ADMIN\n3.Exit")
        type = read_choice("Main Menu")
        if type == 1:
            user_menu()
        elif type == 2:
            print("Admin Menu:\n1.Add Book\n2.Add User\n3.Remove User\n4.Remove Book")
        elif type == 3:
            print("Exiting")
            flag = False
        else:
            print("Please select either 1/2/3")

if __name__ == "__main__":
    main()