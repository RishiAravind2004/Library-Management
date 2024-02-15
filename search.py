import pandas as pd
from tabulate import tabulate
from operations import GetBookID, press_any_key_to_continue
from main import Menu

file_path = "database/db.xlsx"


def Search_Book():
    print("\n\n\t\tSearch Book!\n\n")
    print("1. Searching by Book ID")
    print("2. Searching by Author Name.")
    print("3. Seaching by Book Name.")
    print("\n")
    choice=Book_Choice()
    print (choice)
    if (choice==1):
        search_BookID()
    elif(choice==2):
        search_Author()
    else:
        search_BName()
    press_any_key_to_continue()
    return

    
def Book_Choice():
##    ch=input("Enter Your choice: ")
##    if ch.isdigit():
##        ch=int(ch)
##        if (0 < ch < 4):
##            return ch
##        else:
##            print("\nInvalid Input. Please enter your choice between (1 to 2)!")
##            return Book_Choice()
##    else:
##        print("\nInvalid Input. Please enter a valid integer")
##        return Book_Choice()

    #OR

    try:
        ch = int(input("\nEnter Your choice: "))
        if 0 < ch < 4:
            return ch
        else:
            print("\nInvalid Input. Please enter your choice between (1 to 2)!")
            return Book_Choice()  
    except ValueError:
        print("\nInvalid Input. Please enter a valid integer")
        return Book_Choice() 

def search_BookID():
    #accessing DB and reading data
    db = pd.read_excel(file_path, sheet_name='Books')

    id_data=db[['ID']]
    search_id=GetBookID()
    search_id = str(search_id)

    # Check if the entered bookid is present in the DataFrame (partial match)
    matching_ids = db[db['ID'].astype(str).str.contains(search_id, case=False)]

    req_data = matching_ids[['ID', 'Name', 'Author']]

    if not matching_ids.empty:
        
        Display_Book(req_data)
    else:
        print("Book ID not found in the database.")

        
def search_Author():
    #accessing DB and reading data
    db = pd.read_excel(file_path, sheet_name='Books')

    author_data=db[['Author']]
    search_author_name=input("Enter the author name: ")

    # Check if the entered author name is present in the DataFrame (partial match)
    matching_authors = db[db['Author'].str.contains(search_author_name, case=False)]

    req_data = matching_authors[['ID', 'Name', 'Author']]

    if not matching_authors.empty:
        Display_Book(req_data)
    else:
        print("Author Name not found in the database.")


def search_BName():
    #accessing DB and reading data
    db = pd.read_excel(file_path, sheet_name='Books')

    author_data=db[['Name']]
    search_book_name=input("Enter the book name: ")

    # Check if the entered book name is present in the DataFrame (partial match)
    matching_books = db[db['Name'].str.contains(search_book_name, case=False)]

    req_data = matching_books[['ID', 'Name', 'Author']]

    if not matching_books.empty:
        Display_Book(req_data)
    else:
        print("Book Name not found in the database.")


def Display_Book(req_data):
    # Print the matching rows
    print("\nMatching datas from database:")
    print("\n")
    print(tabulate(req_data, 
        headers=req_data.columns, 
        tablefmt='fancy_grid',
        showindex=False)
    )
    return

if __name__=="__main__":
    Search_Book()
