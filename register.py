#from main import Menu
from operations import GetBookID,confirmation
from db_op import Reg_New_Book_DB
import pandas as pd


def Register_Book():
    
    print("\n\t\tNew Book Registeration!!\n\n")

    while True:
        BookID=GetBookID()
        if BookID==-1: print("Exiting...."); return
        print("Entered: ",BookID)
        result=BookIDcollisionCheck(BookID)
        if (result==1):
            break
    BookName=input("\nEnter the Book Name: ").title()   #the function ".title()" turns the given input as title every letter of first word to capital
    if BookName.lower() in ("-1", "exit"): print("Exiting...."); return
    BookAuthor=input("\nEnter the Book's Author Name: ").title()
    if BookAuthor.lower() in ("-1", "exit"): print("Exiting...."); return
    BookPrice=GetPrice()
        #confirmation
    print("\nPlease check the given details one more to rgeister confirmation!\n")
    print("Book's Name: ",BookName)
    print("Book's ID: ",BookID)
    print("Book's Author Name: ",BookAuthor)
    print("Book's Price: ",BookPrice)
    print("\nYes[Y] to confirm and No[N] to re-enter the details again!")
    
    result=confirmation()
    if(result==1):
        Reg_New_Book_DB(BookID, BookName, BookAuthor, BookPrice)
        print("Do you want to register another book?")
        result=confirmation()
        if(result==1):
            Register_Book()
        else:
            return
    else:
        print("Do you still want to register a new book?")
        result=confirmation()
        if(result==1):
            Register_Book()
        else:
            return


def BookIDcollisionCheck(B_num):
    print("Verifying Book ID....")
    #accessing Database
    db=pd.read_excel("database/db.xlsx",sheet_name="Books")
    
    DBBooksID=db['ID'].tolist() #or "db.ID" and for ".tolist" get every element in ID column as list, db[db['ID'].isin([B_num])] return boolean
    if (B_num in DBBooksID):
        print("The ID is already used for other book. Please re-enter the Book ID!")
        return 0
    else:
        print("ID is Verified!")
        return 1



def GetPrice():
    try:
        price = float(input("\nEnter Book's Price: "))
        if price >= 0:
            return price
        else:
            print("\nInvalid Input. Please enter a valid ammount which is greater then 0!.")
            return GetPrice()
    except:
        print("\nInvalid Input. Please enter a valid ammount.")
        return GetPrice()


if __name__=="__main__":
    Register_Book()
