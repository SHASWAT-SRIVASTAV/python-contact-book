'''
Hey I welcome you to my callbook
i made this callbook while learning python dictionary and system architecture
This project callbook 1.0 will help me get better understanding of python  dictionary and software design 

function my callbook has for right now :-
1.Add contact 
2.Delete
3.Search contact
4.View all contacts
5.Clear callbook


Future Scopes of this callbook:-
1.Having a json file where contacts get stored.(file handling)

2.I will come up with a better UI/UX design in the upcoming version 



'''
def add_contact(callbook):



    contact_name = input("Enter contact name: ")

    # Check if contact already exists
    if contact_name in callbook:

        print("Contact already exists.")
        print("1. Overwrite")
        print("2. Cancel")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            contact_number = int(input("Enter new contact number: "))
            callbook[contact_name] = contact_number
            print("Contact updated successfully.")

        else:
            print("Contact was not modified.")

    else:
        contact_number = int(input("Enter contact number: "))
        callbook[contact_name] = contact_number
        print("Contact added successfully.")

    print("\nCurrent Callbook")
    print("----------------")

    for key, value in callbook.items():
        print(f"{key} -> {value}")
 

    

    
        




def delete_contact(callbook):

    contact_name =input("Enter the name of the person that you wish to delete contact of: ")

    try:

        callbook.pop(contact_name)
        
    except KeyError:
        print("No such contact found in your callbook ")

   

    finally:
        print("Your updated callbook is :- " )
        print(callbook)    
    


def clear(callbook):

    
    callbook.clear()
    print("Your updated callbook is :- " )
    print(callbook)


def  search_contact(callbook):

    contact_name=input("Enter contact that you want to search: ")

    
    contact_number=callbook.get(contact_name,"Contact not found ")
    print(f"contact number: {contact_number}")

      


def view_all(callbook):

    print("Your callbook is :- " )
    for key,value in callbook.items():
        print(key,"->",value) 


def main():

    callbook={}
    flag=1
    while(flag):
        print("---------------------------------------------")
        print("Welcome to callbook by Shaswat Srivastav ")
        print("What do you want to do in your callbook ")
        print("1.Add contact ")
        print("2.Delete contact")
        print("3.Search contact")
        print("4.View all contacts")
        print("5.Clear callbook")
        print("6.Exit")
        print("---------------------------------------------")
      


        choice=int(input("Enter you choice of opeartion on callbook: "))

        match(choice):

            case 1: add_contact(callbook)
            case 2: delete_contact(callbook)
            case 3: search_contact(callbook)
            case 4: view_all(callbook)
            case 5: clear(callbook)
            case 6:
                flag=0
                print("Thank you for using This callbook")

main()
                          






    

            

    









    

    