#returning the book!!!
import config
import pandas as pd
from operations import GetBookID,confirmation
from datetime import datetime, timedelta
from main import Menu

max_fine_rate=config.Max_Fine_Rate

def CheckIn_Book():

    print("\n\t\tBook CheckIn!!\n\n")

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
        if (Selected_Book['Status'].values[0]=='Checked Out'):

            FineAmt=Selected_Book['Fine'].values[0]
            OldDueDate=Selected_Book['Due Date'].values[0]
            today = datetime.now().date()


            OldDueDate = pd.to_datetime(OldDueDate, format='%d-%m-%Y')
            today = pd.to_datetime(today, format='%d-%m-%Y')

            days_overdue = (today - OldDueDate).days

            Newfine = DamageFine = 0


            if days_overdue > 0:
                Newfine = days_overdue * fine_rate_per_day
                print("You due date has passed!!")
                print("Over Due Day Count: ",days_overdue," days")
                print("Old Fine Amount: Rs.",FineAmt)
                print("New Fine Amount: Rs.",Newfine)
                print("Total Fine Amount: Rs.",FineAmt+Newfine)
                #db.loc[selected_book_index[0], 'Fine'] = FineAmt+Newfine
            else:
                print("Returning within the due date!")

            print("\nAre you sure of return of book?")
            result=confirmation()
            if(result==1):
                print("\nCheckIn the book into libarary!!")
                print("Any Damanges in Book??")
                result=confirmation()

                #caluclating book damage amount
                if(result==1):
                    print("Enter the percentage of damange from (1 to 100%) the fine ammout will be calucalted on it!! ")
                    while True:
                        DamageRate=input("Enter Damage Percentage:")
                        if DamageRate.replace('.', '', 1).isdigit():
                            length= len(str(DamageRate))
                            DamageRate=float(DamageRate)
                            if (0<=length and length<=100):
                                break
                            else:
                                print("\nInvalid Input. You have to enter valid percentage from 1 to 100!")
                        else:
                            print("\nInvalid Input. Please enter a valid integer")
                    DamageFine = DamageRate * max_fine_rate
                    print("Fine amount for book damage: ",DamageFine)

                else:
                    print("You are assured their is no damages!!")
                print("\n\nTotal Fine Amount: ", FineAmt+Newfine+DamageFine)

                if ((FineAmt+Newfine+DamageFine)!=0):
                    while True:
                        print("Is fine ammount collected??")
                        result=confirmation()
                        if(result==1):
                            print("Assured fine amount collected!")
                            break
                        else:
                            print("Please collect the fine amount and procedue again!")

                print("Checking in the book.......!!")

                new_details={
                    'Fine': 0,
                    'Status': "Available",
                    'Person Name': None,
                    'Person Mobile Number': None,
                    'Person Address': None,
                    'CheckedOut Date': None,
                    'Due Date': None
                    }

                # Find the index of the row that matches the given book number
                selected_book_index = db.index[db['ID'] == B_num].tolist()
                
                # Check if the book exists in the database
                if selected_book_index:
                    # Get the details of the selected book
                    selected_book = db.loc[selected_book_index[0]]
                    # Update the selected book's details with the new details
                    for key, value in new_details.items():
                        db.loc[selected_book_index[0], key] = value
                    
                    # Save the modified DataFrame back to the database file
                    with pd.ExcelWriter("database/db.xlsx", engine='openpyxl', mode='a', if_sheet_exists="replace") as writer:
                        db.to_excel(writer, sheet_name='Books', index=False)


                print("CheckedIn Successfully....")

                print("Do you want to return another book?")
                result=confirmation()
                if(result==1):
                    CheckIn_Book()
                else:
                    return
                                
            else:
                print("Do you want to return a book?")
                result=confirmation()
                if(result==1):
                    CheckIn_Book()
                else:
                    return
        else:
            print("The book is already in library you can't checkin it!!")
            print("Do you want to return a book?")
            result=confirmation()
            if(result==1):
                CheckIn_Book()
            else:
                return

    else:
        print("Do you want to return a book?")
        result=confirmation()
        if(result==1):
            CheckIn_Book()
        else:
            return
if __name__ == "__main__":
    CheckIn_Book()
