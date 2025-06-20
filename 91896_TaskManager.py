import easygui

task_dictionary = {
    "T1" : {
        "Title" : "Design Homepage",
        "Description" : "Create a mockup of the homepage",
        "Assignee" : "JSM",
        "Priority" : 3,
        "Status" : "In Progress"
    },
    "T2" : {
        "Title" : "Implement Login page",
        "Description" : "Create the Login page for the website",
        "Assignee" : "JSM",
        "Priority" : 3,
        "Status" : "Blocked"
    },
    "T3" : {
        "Title" : "Fix navigation menu",
        "Description" : "Fix the navigation menu to be more user-friendly",
        "Assignee" : "", #"None"???
        "Priority" : 1,
        "Status" : "Not Started"
    },
    "T4" : {
        "Title" : "Add payment processing",
        "Description" : "Implement payment processing for the website",
        "Assignee" : "JLO",
        "Priority" : 2,
        "Status" : "In Progress"
    },
    "T5" : {
        "Title" : "Create an About Us page",
        "Description" : "Create a page with information about the company",
        "Assignee" : "BDI",
        "Priority" : 1,
        "Status" : "Blocked"
    }
}

team_member_dictionary = {
    "JSM" : {
        "Name" : "John Smith",
        "Email" : "John@techvision.com",
        "Tasks assigned" : ["T1","T2"],
    },
    "JLO" : {
        "Name" : "Jane Love",
        "Email" : "Jane@techvision.com",
        "Tasks assigned" : ["T4"],
    },
    "BDI" : {
        "Name" : "Bob Dillon",
        "Email" : "Bob@techvision.com",
        "Tasks assigned" : ["T5"],
    }
}

def add_new_task():
    """"Using this function, the users will be able to add a new task to the 
        task list, assign a team member, priority status and discription"""
    edit_or_add_multenterbox(["","","","",""],task_dictionary,"Add a new task")

def edit_or_add_multenterbox(initial_values, accessing_dictionary,title):
    """"IDK"""
    prompt = "Please enter the desired information below..."
    feild_value_types = []
    entering_fields = []
    for main_dictionary_id, dictionary_definitions in accessing_dictionary.items():
        for dictionary_key in dictionary_definitions:
            if dictionary_key not in entering_fields:
                entering_fields.append(dictionary_key)
    print(feild_value_types)            
    task_details = easygui.multenterbox(prompt,title,entering_fields,
        initial_values)
    if task_details == None:
        main_menu()
    #for entered_value in task_details:
    #    if entered_value == None:
    #        print("None")

#def update_task():

#def search():

#def generate_report():

def print_tasks(sort_status, sort_direction):
    """"Print tasks"""""
    choicebox_title = "Current tasks"
    choicebox_text = [f"Sorted {sort_status}:"]
    choicebox_text.append("==============================================================")
    choicebox_sort_options = ["By Creation", "By Priority", "By Status", "By Assignee", "Exit"]

    if sort_status == "By Creation":
        for task_id, task_details in task_dictionary.items():
            choicebox_text.append(f"\n[ {task_dictionary[task_id]['Title']} ]")
            for task_key, task_value in task_details.items():
                if task_key != "Title":
                    choicebox_text.append(f"\t{task_key}: {task_value}")
    
    sort_or_exit = easygui.choicebox("\n".join(choicebox_text), choicebox_title, choices=choicebox_sort_options)
    if sort_or_exit == None or sort_or_exit == "Exit":
        main_menu()
    else:
        buttonbox_text = "Sort by: " + sort_or_exit
        buttonbox_choices = ["Ascending", "Descending", "Exit"]
        sort_direction_choice = easygui.buttonbox(buttonbox_text, choices=buttonbox_choices)
        if sort_direction == None or sort_direction == "Exit":
            print_tasks(sort_status, sort_direction)
        else:
            print_tasks(sort_or_exit, sort_direction_choice)

#def check_if_digit(digit,max_value,min_value):

#def check_if_string(string):

def main_menu():
    print_tasks("By Creation", "Ascending")

main_menu()