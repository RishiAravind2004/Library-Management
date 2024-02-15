from main import Menu
from db_op import BookIDCheckInDB, CheckOut_Book_DB
from operations import GetBookID,confirmation
import pandas as pd
def CheckOut_Book():

    print("\n\t\tBook CheckOut!!\n\n")

    print("Enter the book you want to checkout from library!!")
    while True:
        B_num=GetBookID()
        print("Entered: ",B_num)
        result, Selected_Book, db= BookIDCheckInDB(B_num)
        if (result==1):
            break
    print(B_num)
    if(result==1):      
        print("\nBook information for the given Book ID\n")
        print("Book ID: ",int(Selected_Book['ID'].values[0]))
        print("Book Name: ",Selected_Book['Name'].values[0])
        print("Book Author: ",Selected_Book['Author'].values[0])
        print("Are you sure to checkout this book?")
        conf_result=confirmation()
        if (conf_result==1):
            #getting checkouter details
            print("\nCheckOuter's Details!")
            Member_Name=input("\nPerson's Name: ").title()
            Member_No=Get_Mobile_Num()
            Member_Address=input("Person's Address: ").title()

            print("Checking Book with person\'s detail")
            print("\nBook Information\n")
            print("Book ID: ",int(Selected_Book['ID'].values[0]))
            print("Book Name: ",Selected_Book['Name'].values[0])
            print("Book Author: ",Selected_Book['Author'].values[0])
            print("Are you sure to checkout this book?")
            print("\nCheckOuter's Information\n")
            print("Name: ",Member_Name)
            print("Mobile Number: ",Member_No)
            print("Address: ",Member_Address)
            print("Press yes to checkout this book.....")
            conf_result=confirmation()
            if (conf_result==1):
                details={
                    'Person Name': Member_Name,
                    'Person Mobile Number': Member_No,
                    'Person Address':Member_Address
                    }
                CheckOut_Book_DB(B_num, details)
                print(f"Checkouted \"{Selected_Book['Name'].values[0]}\" Book from Library!")
            else:
                print(f"Not checkouting the \"{Selected_Book['Name'].values[0]}\" book...")   
            print("Do you still want to checkout a book?")
            result=confirmation()
            if(result==1):
                CheckOut_Book()
            else:
                return
    else:
        print("Do you still want to checkout a book?")
        result=confirmation()
        if(result==1):
            CheckOut_Book()
        else:
            return


def Get_Mobile_Num():
##    M_num=input("Person's Mobile Number:")
##    if M_num.isdigit():
##        length= len(str(M_num))
##        M_num=int(M_num)
##        if (length == 10):
##            return M_num
##        else:
##            print("\nInvalid Input. You have entered mobile number length of ",length,". Please enter the mobile number lenth of ",10,".")
##            return Get_Mobile_Num()
##    else:
##        print("\nInvalid Input. Please enter a valid integer")
##        return Get_Mobile_Num()

    #OR
    try:
        M_num=int(input("Person's Mobile Number: "))
        if (len(str(M_num)) == 10):
            return M_num
        else:
            print(f"\nInvalid Input. You have entered mobile length of {len(str(M_num))}. Please enter the book number lenth of 10.")
            return Get_Mobile_Num()
    except ValueError:
        print("\nInvalid Input. Please enter a valid integer")
        return Get_Mobile_Num()



if __name__=="__main__":
    CheckOut_Book()

    

