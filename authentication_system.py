import time
import re

def register():

    # receive info from user
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    password = input("Password: ")
    confirm_password = input("Confirm password: ")
    mobile_phone = input("Mobile phone: ")
    
    # set id for user account 
    user_id = round(time.time())
    
    # store registeration data in text file
    data = f"{user_id}:{first_name}:{last_name}:{email}:{password}:{confirm_password}:{mobile_phone}\n"
    

    # verify name 
    if first_name.isdigit() or first_name.isspace() :
        print("\ninvalid name.....please enter valid name: ")
        register()
    else:
        # validate email
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if (re.search(regex, email)):
            # validate password
            if password == confirm_password:
                # Phone Validation
                if re.match("^01[0125][0-9]{8}$", mobile_phone):
                    stored_data = open("users.txt","a")
                    stored_data.write(data)
                    stored_data.close()
            else:
                print("\nYour password is invalid.....please enter valid password: ")
                register()
        else:
            print("Invalid Email.....please enter valid email: ")
            register()

def login_page():

    # receive input from user
    user_email = input("Email: ")
    user_password = input("Password: ")
    
    # read file data
    stored_data = open("users.txt","r")
    users = stored_data.readlines()
    
    # verify login
    for user in users:
        user_data = user.split(":")
        if user_email == user_data[3]:
            if user_password == user_data[4] :
                print("login successful")
                user_id = user_data[0]
                print(f"userID: {user_id}")
            
            else:
                print("invalid username and password")
                login_page()

def main():
    
    # receive choice from user
    choice = input("\nPlease choose 1 for Registeration and choose 2 for login :\n")
    
    # registeration
    if choice == "1":
        return register()
    
    # login
    elif choice == "2":
        return login_page()
    else:
        print("\nPlease choose From menu")
main()