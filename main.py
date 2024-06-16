'''

        Local Network Library Management System
        
        
'''


def Menu():
    print("\n############################################################################")
    print("\n\n\t\tLocal Network Library Management Sytem!!")
    print("\n\n\tNotes: 1.For storing the datas i used excel sheet instead of database for simple understanding for beginners")
    print("\t       2.Multiple copies of books are managed by book id and no seperate feature to multiple copies of book")
    print("\n")
    print("\tSouce Code/Repo Link: https://github.com/RishiAravind2004/Library-Management")
    print("\n")
    print("\n############################################################################")
    print("\n")
    print("Checking for Existing DataBase......")

    from db_op import check_file_exists
    from operations import press_any_key_to_continue

    check_file_exists()
    press_any_key_to_continue()
    print("\n")
    
    Run = True
    while(Run):
        print("\n\n\t\tLibrary Menu\n\n")
        print("1.Register New Book")
        print("2.Unregister Book")
        print("3.Book Check IN(Return)")
        print("4.Book Check OUT")
        print("5.Book Renewal")
        print("6.Search Book")
        print("7.Listing Book")
        print("8.Book Info")
        print("9.Exit")
        choice=GetChoice()

        #Executing the give choice given by user
        if (choice == 1):
            print("\nChoosed Register New Book!")
            from register import Register_Book
            Register_Book()
        elif (choice == 2):
            print("\nChoosed Unrgister Book!")
            from unregister import Unregister_Book
            Unregister_Book()          
            
        elif (choice == 3):
            print("\nChoosed Book Check IN!")
            from checkin import CheckIn_Book
            CheckIn_Book()

        elif (choice == 4):
            print("\nChoosed Book Check OUT!")
            from checkout import CheckOut_Book
            CheckOut_Book()

        elif (choice == 5):
            print("\nChoosed Book Renewal!")
            from renewal import Renewal
            Renewal()  

        elif (choice == 6):
            print("\nChoosed Searching Book!")
            from search import Search_Book
            Search_Book()

        elif (choice == 7):
            print("\nChoosed Listing Book!")
            from listing import List_Books
            List_Books()

        elif (choice == 8):
            print("\nChoosed Book Info!")
            from info import Book_Info
            Book_Info() 

        elif (choice == 9):
            print("\nChoosed Exit!")
            Run=False

        else:
            print("\nNo Valid Choice!")





def GetChoice():

    try:
        ch = input("\nEnter Your choice: ")
        if ch.lower() in ("-1", "exit"): print("Exiting...."); exit()
        ch=int(ch)
        if 0 < ch < 10:
            return ch
        else:
            print("\nInvalid Input. Please enter your choice between (1 to 9)!")
            return GetChoice()
    except ValueError:
        print("\nInvalid Input. Please enter a valid integer")
        return GetChoice()

    #OR

##    ch=input("Enter Your choice: ")
##    if ch.isdigit():
##        ch=int(ch)
##        if (0 < ch < 10):
##            return ch
##        else:
##            print("\nInvalid Input. Please enter your choice between (1 to 9)!")
##            return GetChoice()
##    else:
##        print("\nInvalid Input. Please enter a valid integer")
##        return GetChoice()

        
if __name__=="__main__":
    Menu()
