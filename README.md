# Crowd-Funding-console-app
This repository contains python code to create a console app to start fund raise projects.

## Overview
### Authentication System:
- Registration:
  - First name
  - Last name
  - Email
  - Password
  - Confirm password
  - Mobile phone [validated against Egyptian phone numbers]
- Login:
  - The user should be able to login after activation using his email and password

### Projects:
- The user can create a project fund raise campaign which contains:
  - Title
  - Details
  - Total target (i.e 250000 EGP)
  - Set start/end time for the campaign (validate the date formula)
- User can view all projects
- User can edit his own projects
- User can delete his own project
- User can search for a project using date

## Prerequisites
Before running the script, you will need to have the following:
- interpreter correctly installed on your system.
- python installed on your system

## To get started:
Clone this repository to your local machine.
```
git clone https://github.com/AbdulrahmanElfeki/Crowd-Funding-console-app
```
To run Authrntication System:
```
python3 authentication_system.py
```
to create projects:
```
python3 projects_app.py
```
## To view Project data:
data is stored in users.txt, project_data.txt
