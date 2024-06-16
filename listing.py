from operations import press_any_key_to_continue
import pandas as pd
# Importing the tabulate Function
from tabulate import tabulate
from main import Menu

#refer here for example for table: "https://datagy.io/create-table-in-python-tabulate/"
db_path = "database/db.xlsx"

def List_Books():

    #accessing DB and reading data
    db = pd.read_excel(db_path, sheet_name='Books')

    req_data=db[['ID', 'Name', 'Author', 'Status']]

    if req_data.empty:
        print('\n######################################')
        print('\nNo Data Found In DataBase!\n')
        print('\n######################################')
    else:
        print("Here the list! ")
        print("\n")
        print(tabulate(req_data, 
                headers=req_data.columns, 
                tablefmt='fancy_grid',
                showindex=False)
        )

    
    #after displaying press anykey to continueeeee
    press_any_key_to_continue()
    #returning to menu after pressing the key
    return
    
if __name__=="__main__":
    List_Books()
