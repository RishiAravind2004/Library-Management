from operations import GetBookID,confirmation,press_any_key_to_continue
from main import Menu
import pandas as pd


def Book_Info():

    print("\n\t\tBook Information!!\n\n")

    print("Enter the book you want to checkin into the library!!")

    while True:
        B_num=GetBookID()
        break
    print("Entered: ",B_num)

    db=pd.read_excel("database/db.xlsx",sheet_name="Books")

    DBBooksID=db['ID'].tolist() #or "db.ID" and for ".tolist" get every element in ID column as list, db[db['ID'].isin([B_num])] return boolean
    if (B_num in DBBooksID):
        print("ID was founded in database!")
        Selected_Book = db[db['ID'] == B_num] #selecting the book #get details in the specific rows, It is the selected book using id
        if (Selected_Book['Status'].values[0]=='Available'):

            print("\n\n\t\tBook Infomation\n\n")

            print("Book's ID: ", int(Selected_Book['ID'].values[0]))
            print("Book's Name: ", Selected_Book['Name'].values[0])
            print("Book's Author Name: ", Selected_Book['Author'].values[0])
            print("Status: ", Selected_Book['Status'].values[0])
            print("Registered Date: ", str(Selected_Book['RegDate'].values[0]))

        else:

            print("\n\n\t\tBook Infomation\n\n")

            print("Book's ID: ", int(Selected_Book['ID'].values[0]))
            print("Book's Name: ", Selected_Book['Name'].values[0])
            print("Book's Author Name: ", Selected_Book['Author'].values[0])
            print("Status: ", Selected_Book['Status'].values[0])
            print("Registered Date: ", str(Selected_Book['RegDate'].values[0]))
            print("Checked Out Date: ", Selected_Book['CheckedOut Date'].values[0])
            print("Due Date: ", str(Selected_Book['Due Date'].values[0]))
            print("Fine Amount: ", Selected_Book['Fine'].values[0])

            print("\nChecked Out Person Details!\n")

            print("Person's Name: ", Selected_Book['Person Name'].values[0])
            print("Person's Mobile Number: ", int(Selected_Book['Person Mobile Number'].values[0]))
            print("Person's Address: ", Selected_Book['Person Address'].values[0])

        press_any_key_to_continue()
        print("Still do you want to check information for any other book?")
        result=confirmation()
        if(result==1):
            Book_Info()
        else:
            return
  

    else:
        print("Book ID was not founded in database")
        print("Still do you want to check information for any other book?")
        result=confirmation()
        if(result==1):
            Book_Info()
        else:
           return

if __name__=="__main__":
    Book_Info()
