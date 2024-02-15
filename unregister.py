from db_op import BookIDCheckInDB, UnReg_Book_DB
from main import Menu
from operations import GetBookID,confirmation
import pandas as pd

def Unregister_Book():

    print("\n\t\tBook Unregisteration!!\n\n")

    print("Enter the book you want to unregister currently available in library!!")
    while True:
        B_num=GetBookID()
        print("Entered: ",B_num)
        result, Selected_Book, db= BookIDCheckInDB(B_num)
        if (result==1):
            break
    print(B_num)
    if(result==1):      
        print("\nBook information for the given Book ID\n")
        print("Book ID: ",Selected_Book['ID'].values[0])
        print("Book Name: ",Selected_Book['Name'].values[0])
        print("Book Author: ",Selected_Book['Author'].values[0])
        print("Are you sure to delete this book?")
        conf_result=confirmation()
        if (conf_result==1):
            print("Un Registering book from library database!")
            UnReg_Book_DB(B_num,db)
            print("Do you still want to unregister a book?")
            result=confirmation()
            if(result==1):
                Unregister_Book()
            else:
                return
    else:
        print("Do you still want to unregister a book?")
        result=confirmation()
        if(result==1):
            Unregister_Book()
        else:
            return



if __name__ == "__main__":
    Unregister_Book()
