import config

BookIDLength=config.BookIDLength




#this def is used to get input from user for book id
def GetBookID():
##    B_num=input("\nEnter the Book ID: ")
##    if B_num.lower() in ("-1", "exit"): print("Exiting...."); return -1
##    if B_num.isdigit():
##        length= len(str(B_num))
##        B_num=int(B_num)
##        if (length == BookIDLength):
##            return B_num
##        else:
##            print("\nInvalid Input. You have entered book id length of ",length,". Please enter the book number lenth of ",BookIDLength,".")
##            return GetBookID()
##    else:
##        print("\nInvalid Input. Please enter a valid integer")
##        return GetBookID()

    #OR
    try:
        B_num=int(input("\nEnter the Book ID: "))
        if B_num==-1: print("Exiting...."); return -1
        if (len(str(B_num)) == BookIDLength):
            return B_num
        else:
            print(f"\nInvalid Input. You have entered book id length of {len(str(B_num))}. Please enter the book number lenth of {BookIDLength}.")
            return GetBookID()
    except ValueError:
        print("\nInvalid Input. Please enter a valid integer")
        return GetBookID()


#Confirmation
def confirmation():
    
##    confirm=input("Yes[Y]/No[N]?: ")
##    if (len(confirm)==1):
##        if ((confirm.lower())=='y' or (confirm.lower())=='n'):
##            if ((confirm.lower())=='y'):
##                print("You have pressed YES!")
##                return 1
##            else:
##                print("You have pressed NO!")
##                return 0
##        else:
##            print("\nInvalid Input. Please enter Yes[Y]/No[N]!")
##            return confirmation()
##    else:
##        print("\nInvalid Input. You have to enter Yes[Y]/No[N]!")
##        return confirmation()

    #OR

    try:
        confirm = input("Yes[Y]/No[N]?: ")
        if len(confirm) == 1:
            if confirm.lower() == 'y' or confirm.lower() == 'n':
                if confirm.lower() == 'y':
                    print("You have pressed YES!")
                    return 1
                else:
                    print("You have pressed NO!")
                    return 0
            else:
                raise ValueError("nInvalid Input. Please enter 'Yes[Y]' or 'No[N]'.")
        else:
            raise ValueError("\nInvalid Input. You have to enter 'Yes[Y]' or 'No[N]'.")
    except ValueError:
        print("\nInvalid Input. You have to enter 'Yes[Y]' or 'No[N]'.")
        return confirmation()

# Press any key to continue....
import keyboard

def press_any_key_to_continue():
    print("Press any key to continue...")
    keyboard.read_event()  # Waits for any key press
    print("Continuing...")

    #OR
    
##    print("Press any key to continue...")
##    try:
##        event = keyboard.read_event()  # Waits for any key press
##        if event.event_type == keyboard.KEY_DOWN:
##            print("Continuing...")
##    except KeyboardInterrupt:
##        print("\nContinuing...")  # Print "Continuing..." if Ctrl+C is pressed



if __name__=="__main__":
    GetBookID()
