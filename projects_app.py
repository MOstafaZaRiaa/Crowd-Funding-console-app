import time
from math import *

# the user can create his projects using ID
def create():

    # receive project details from user
    title = input("Title: ")
    details = input("Details: ")
    total_target = input("Total target: ")
    if total_target.isdigit():
        total_target=int(total_target)
    else:
        print("Invalid value")
    start_time = input("Start Date: ")
    end_time = input("End Date: ")
    user_id = input("please enter your ID:")
    if user_id.isdigit():
        user_id=int(user_id)
    else:
        print("Invalid value")
    
    # store project info in text file
    project_info =f"{user_id}:{title}:{details}:{total_target}:{start_time}:{end_time}\n"
    # create project
    try:
        valid_date1 = time.strptime(start_time, '%m/%d/%Y')
        valid_date2 = time.strptime(end_time, '%m/%d/%Y')
        
        if valid_date1 and valid_date2:
            project_data = open("project_data.txt", "a")
            project_data.write(project_info)
            project_data.close()
            print('Your project is created successfully')
        else:
             print("\nYour data is invalid")

    except ValueError:
        print('Invalid date!')
        create()

# the user can view for his projects using ID
def view():
    user_id= input("please enter your ID to view your projects: ")
    if user_id.isdigit():
        user_id=int(user_id)
    else:
        print("Invalid value")
    # read projects file
    project_data=open("project_data.txt","r")
    projects = project_data.readlines()
    for index, project in enumerate(projects):
            project_details = project.strip('\n')
            project_details = project_details.split(':')
            if project_details[0] == id:
                selected_project = index
                break
    else:
        print("no project for you")
        view()
    
    print(projects[selected_project])

# can delete for his projects using ID
def delete():
    
    user_id= input("please enter your ID to view your projects: ")
    if user_id.isdigit():
        user_id=int(user_id)
    else:
        print("Invalid data")
    # display user projects to select from
    view()
    # ask the user to enter the title
    title = input("Please Enter Project title to delete:\n")
    
    # read all lines
    project_data = open("project_data.txt", "r")
    projects = project_data.readlines()
    
    # delete selected project
    for index, project in  enumerate(projects) :
        project_details = project.strip("\n").split(":")
        if project_details[0] == user_id :
            selected_project=index
            break
           
    else:
        print("project name does not exist\n")
        delete()
    
    del projects[selected_project]
    
    # update text file
    project_data = open("project.txt", 'w')
    project_data.writelines(project)
    project_data.close()
    print("project is deleted successfully\n")

# the user can edit it's project and add new details
def edit():
    view()
    delete()
    # recieve new info from user to update
    title = input("Title: ")
    details = input("Details: ")
    total_target = input("Total target: ")
    start_time = input("Start Date: ")
    end_time = input("End Date: ")
    user_id = round(time.time())
    project_info = f"{user_id}:{title}:{details}:{total_target}:{start_time}:{end_time}\n"
    try:
        valid_date1 = time.strptime(start_time, '%m/%d/%Y')
        valid_date2 = time.strptime(end_time, '%m/%d/%Y')
        
        if valid_date1 and valid_date2:
            project_data = open("project_data.txt", "a")
            project_data.write(project_info)
            project_data.close()
            print('Your project is edited successfully')
            main()
        else:
             print("\nYour data is invalid")

    except ValueError:
        print('Invalid date!')
        edit()
    
# the user can search for his project
def search():
    project_date = input("Write project date (mm/dd/yyyy)\n ")
    try:
        valid_date = time.strptime(project_date, '%m/%d/%Y')
        if valid_date:
                project_data=open("project_data.txt","r")
                projects = project_data.readlines()

                # search for poject
                for project in projects:
                    project.strip("\n").split(":")
                    if project_date == project[4] or project_date == project[5]:
                        print("\nYour project information: \n")
                        print(project)
                    else:
                        print("project does not exist\n")
                        search()
        
        else:
            print("Your data is invalid\n")
    
    except ValueError:
        print('Invalid date!')

def main():
    
    # display options for user
    print("\n\n 1) Create Project \n 2) View All Projects \n 3) Edit Project \n 4) Delete Project \n 5) Search For Project")
    
    # receive option from user
    choice = input("Please choose from menu\n")
    if choice == "1":
        create()
    elif choice == "2":
        view()
    elif choice == "3":
        edit()
    elif choice == "4":
        delete()
    elif choice == "5":
        search()
    else:
        print("\nPlease choose From menu")
    main()
main()