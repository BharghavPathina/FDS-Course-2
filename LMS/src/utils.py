'''

'''

from config import LMS
def read_choice(purpose):
    flag2 = True
    while flag2:
        try:
            type = int(input(f"Please enter options for {purpose}")) ## Explicit Type Casting
            flag2 = False
        except Exception as e:
            print(f"You have entered wrong for {purpose}")

    return type


def user_menu():

    flag  = True
    while flag:
        print("User Menu:\n1. STUDENT\n2. TEACHER\n3.EXIT")
        choice = read_choice("User Menu")
        if choice == 1:
            print("Student Menu:\n1.C Language\n2. Rich Dad Poor Dad\n3. Neural Networks")
            
        elif choice == 2:
            print("Teach Menu:\n1. Artificial Intelligence\n2. Machine Learning\n3. Advanced C\n4. Deep Learning")
        elif choice == 3:
            flag = False
            print("Returning back to Main Menu")
        else:
            print("WRONG INPUT")

def add_book():

    print("Welcome to Adding Books..")
    flag = True
    while flag:
        print("Do you want add a book..y/n")
        choice = input()
        if choice == "y":
            bookName = input("Book Name:")
