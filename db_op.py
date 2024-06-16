import pandas as pd
import os
from datetime import datetime, timedelta

db_dir = "database"
db_path = os.path.join(db_dir, "db.xlsx")

def check_file_exists():
    if os.path.exists(db_path):
        print("Database exists!")
        return
    else:
        print("Database does not exist. Creating a new one...")
        create_database()

def create_database():
    # Create DataFrame for the 'Books' sheet
    data_sheet1 = {
        'ID': [],
        'Name': [],
        'Author': [],
        'Status': [],
        'RegDate': [],
        'Price': [],
        
        'Fine': [],
        'CheckedOut Date': [],
        'Due Date': [],
        'Person Name': [],
        'Person Mobile Number': [],
        'Person Address': []
    }
    df_sheet1 = pd.DataFrame(data_sheet1)

    # Create the database directory if it doesn't exist
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    # Write DataFrame to Excel
    with pd.ExcelWriter(db_path, engine='xlsxwriter') as writer:
        df_sheet1.to_excel(writer, sheet_name='Books', index=False)

    print("New database created successfully.")

    return


def Reg_New_Book_DB(BooID, BookName, BookAuthor, BookPrice):
    # Import necessary libraries
    from datetime import datetime
    import pandas as pd

    # Current Time
    current_date = datetime.now()

    # Accessing DB
    db = pd.read_excel(db_path, sheet_name='Books')

    # Create a DataFrame with the new values
    data = {'ID': [BooID],
            'Name': [BookName],
            'Author': [BookAuthor],
            'Status': ["Available"],
            'RegDate': [current_date.strftime("%d-%m-%Y")],
            'Price': [BookPrice]
            }
    new_data_df = pd.DataFrame(data)

    # Check for empty or all-NA columns in the new data DataFrame
    non_empty_columns_new = new_data_df.columns[new_data_df.notna().any()].tolist()
    new_data_df = new_data_df[non_empty_columns_new]

    # Check for empty or all-NA columns in the existing DataFrame
    non_empty_columns_db = db.columns[db.notna().any()].tolist()
    db = db[non_empty_columns_db]

    # Append the new data to the existing DataFrame
    New_Combined_df = pd.concat([db, new_data_df], ignore_index=True)

    # Write the combined DataFrame back to the Excel file
    with pd.ExcelWriter(db_path, engine='openpyxl', mode='a', if_sheet_exists="replace") as writer:
        New_Combined_df.to_excel(writer, sheet_name='Books', index=False)

    print("New Books information datas are added to Database!!")

    return



def UnReg_Book_DB(B_num,db):
    db=pd.read_excel("database/db.xlsx",sheet_name="Books")
    selected_Book = db[db['ID'] == B_num]
    BookName=selected_Book['Name'].values[0]
    new_db = db.drop(db[db['ID'] == B_num].index)
    with pd.ExcelWriter("database/db.xlsx", engine='openpyxl', mode='a',if_sheet_exists="replace") as writer:
        new_db.to_excel(writer, sheet_name='Books', index=False)
    return print("Successfully unregister book: ", BookName)




def BookIDCheckInDB(B_num):
    print("Verifying Book ID....")
    #accessing Database
    db=pd.read_excel("database/db.xlsx",sheet_name="Books")
    
    DBBooksID=db['ID'].tolist() #or "db.ID" and for ".tolist" get every element in ID column as list, db[db['ID'].isin([B_num])] return boolean
    if (B_num in DBBooksID):
        print("ID was founded in database!")
        Selected_Book = db[db['ID'] == B_num] #selecting the book #get details in the specific rows, It is the selected book using id
        if (Selected_Book['Status'].values[0]=='Available'):
            return 1, Selected_Book, db
        else:
            print("The Book is not currently available in library it is checked out!!")
            return 0, None, None
    else:
        print("ID was not founded in database!")
        return 0, None, None


def CheckOut_Book_DB(B_num, new_details):

    #setting checkedout and due date
    today = datetime.now().date()
    
    # Add 15 days to today's date
    due_date = today + timedelta(days=15)

    today=today.strftime("%d-%m-%Y")
    due_date=due_date.strftime("%d-%m-%Y")

    #updating value to dict of details
    new_details.update({'Status': 'Checked Out',
                        'CheckedOut Date': today,
                        'Due Date': due_date,
                        'Fine': 0
                        })

    # Read the database file
    db = pd.read_excel("database/db.xlsx", sheet_name="Books")
    
    # Find the index of the row that matches the given book number
    selected_book_index = db.index[db['ID'] == B_num].tolist()
    
    # Check if the book exists in the database
    if selected_book_index:
        # Get the details of the selected book
        selected_book = db.loc[selected_book_index[0]]
        
        # Update the selected book's details with the new details
        for key, value in new_details.items():
            value = str(value)
            db.loc[selected_book_index[0], key] = value
        
        # Save the modified DataFrame back to the database file
        with pd.ExcelWriter("database/db.xlsx", engine='openpyxl', mode='a', if_sheet_exists="replace") as writer:
            db.to_excel(writer, sheet_name='Books', index=False)
        
        print("Doneee.....")
        print("\n")
        print("Due Date: ", due_date)
        print("\n")
    else:
        print(f"Book with ID {book_id} not found in the database")




if __name__ == "__main__":
    check_file_exists()
