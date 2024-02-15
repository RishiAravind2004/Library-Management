import pandas as pd
from operations import GetBookID, confirmation
from datetime import datetime, timedelta
import config

fine_rate_per_day = config.Fine_Rate_Per_Day

def Renewal():
    print("\n\t\tBook Renewal!!\n\n")

    print("Enter the book you want to renew:")
    B_num = GetBookID()  # Assuming GetBookID function returns a valid book ID
    print("Entered Book ID:", B_num)

    db = pd.read_excel("database/db.xlsx", sheet_name="Books")

    if B_num in db['ID'].values:
        print("ID was found in the database!")
        selected_book = db.loc[db['ID'] == B_num].iloc[0]

        if selected_book['Status'] == 'Checked Out':
            old_fine_amt = selected_book['Fine']
            old_due_date = selected_book['Due Date']

            today = datetime.now().date()
            new_due_date = today + timedelta(days=15)
            db.loc[selected_book.name, 'Due Date'] = new_due_date.strftime("%d-%m-%Y")

            old_due_date = pd.to_datetime(old_due_date, format='%d-%m-%Y')
            today = pd.to_datetime(today, format='%d-%m-%Y')

            days_overdue = (today - old_due_date).days

            if days_overdue > 0:
                new_fine = days_overdue * fine_rate_per_day
                print("Your due date has passed.")
                print("Overdue Day Count:", days_overdue, "days")
                print("Old Fine Amount: Rs.", old_fine_amt)
                print("New Fine Amount: Rs.", new_fine)
                total_fine_amount = old_fine_amt + new_fine
                print("Total Fine Amount: Rs.", total_fine_amount)
                db.loc[selected_book.name, 'Fine'] = total_fine_amount

            else:
                print("Renewed within the due date!")

            print("\nDue Date has been extended to:", new_due_date.strftime('%d-%m-%Y'))

            # Save the modified DataFrame back to the database file
            with pd.ExcelWriter("database/db.xlsx", engine='openpyxl', mode='a', if_sheet_exists="replace") as writer:
                db.to_excel(writer, sheet_name='Books', index=False)

            print(f"Due date for the Book ID {B_num} was successfully renewed!")
            print("Do you want to renew another book?")
            result = confirmation()
            if result == 1:
                Renewal()
            else:
                return  # Assuming Menu() function is defined elsewhere
        else:
            print("The book is currently available in the library so you can't renew it.")
            print("Do you still want to renew a book?")
            result = confirmation()
            if result == 1:
                Renewal()
            else:
                return  # Assuming Menu() function is defined elsewhere
    else:
        print("ID was not found in the database!")
        print("Do you still want to continue?")
        result = confirmation()
        if result == 1:
            Renewal()
        else:
            return  # Assuming Menu() function is defined elsewhere

if __name__ == "__main__":
    Renewal()
