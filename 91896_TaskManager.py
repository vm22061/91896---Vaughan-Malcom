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

preassigned_values = ["Assignee", "Priority", "Status"]
high_to_low_priority_values = ["3","2","1"]

def add_new_task():
    """"Using this function, the users will be able to add a new task to the 
        task list, assign a team member, priority status and discription"""
    edit_or_add_multenterbox([],"Add a new task",None)

def edit_or_add_multenterbox(initial_values,title,edit_or_add):
    """"IDK"""
    prompt = "Please enter the desired information below..."
    entering_fields = []
    for main_dictionary_id, dictionary_definitions in task_dictionary.items():
        for dictionary_key in dictionary_definitions:
            if dictionary_key not in entering_fields:
                if dictionary_key not in preassigned_values:
                    entering_fields.append(dictionary_key)      
    task_details = easygui.multenterbox(prompt,title,entering_fields,
        initial_values)
    if task_details == None:
        main_menu()
    for entering in task_details:
        if entering == '':
            easygui.msgbox("Please fill in all fields...")
            edit_or_add_multenterbox(task_details,title,edit_or_add)
    if edit_or_add == None:
        preassigned_value_choiceboxs([],[],[],[],-1,edit_or_add)
    else:
        preassigned_value_choiceboxs(task_dictionary[edit_or_add]["Assignee"],
        task_dictionary[edit_or_add]["Priority"],
        task_dictionary[edit_or_add]["Status"],-1,edit_or_add)


def preassigned_value_choiceboxs(preselected_assignee,preselected_priority,
preselected_status,repeat_iteration,edit_or_add):
    repeat_iteration += 1
    if repeat_iteration > 2:
        if edit_or_add != None:
            easygui.msgbox("A new task has been successfully added!\
                \n\nReturning to main menu...")
        else:
            easygui.msgbox(f"Task {edit_or_add} has been successsfully \
                updated!\n\nReturning to main menu...")
    choicebox_subject = preassigned_values[repeat_iteration]
    choicebox_prompt = f"Set the task's {choicebox_subject}..."
    choicebox_title = f"Set task's {choicebox_subject}"
    #choicebox_choices = 
    choicebox_preselect = [preselected_assignee,preselected_priority,
    preselected_status][repeat_iteration]
    assignee_choices = []
    preselected_assignee = []
    if edit_or_add != None:
      preselected_assignee = edit_or_add
    for team_member_id in team_member_dictionary:
        assignee_full_name = team_member_dictionary[team_member_id]["Name"]
        assignee_choices.append(f"{team_member_id} : {assignee_full_name}")
    assignee_chosen = easygui.choicebox("Set an assignee or continue if \
        no assignee:","Choose an assignee",assignee_choices,
        preselected_assignee)
    priority_chosen = easygui.buttonbox("Set the tasks priority \
        (set in order of high to low priority)","Set priority",
        high_to_low_priority_values)
    #if priority_chosen == None:
    status_chosen = easygui.buttonbox("Set the tasks current status")

#def update_task():

#def search():

#def generate_report():

def print_tasks(sort_status, sort_direction):
    """"Print tasks"""""
    choicebox_title = "Current tasks"
    choicebox_text = [f"Sorted {sort_status}:"]
    choicebox_text.append("===================================================\
        ===========")
    choicebox_sort_options = ["By Creation","By Priority","By Status",
    "By Assignee","Exit"]

    if sort_status == "By Creation":
        for task_id, task_details in task_dictionary.items():
            choicebox_text.append(f"\n[ {task_dictionary[task_id]['Title']} ]")
            for task_key, task_value in task_details.items():
                if task_key != "Title":
                    choicebox_text.append(f"\t{task_key}: {task_value}")
    
    sort_or_exit = easygui.choicebox("\n".join(choicebox_text),choicebox_title,
    choices=choicebox_sort_options)
    if sort_or_exit == None or sort_or_exit == "Exit":
        main_menu()
    else:
        buttonbox_text = "Sort by: " + sort_or_exit
        buttonbox_choices = ["Ascending", "Descending", "Exit"]
        sort_direction_choice = easygui.buttonbox(buttonbox_text,
        choices=buttonbox_choices)
        if sort_direction == None or sort_direction == "Exit":
            print_tasks(sort_status, sort_direction)
        else:
            print_tasks(sort_or_exit, sort_direction_choice)

#def check_if_digit(digit,max_value,min_value):

#def check_if_string(string):

def main_menu():
    print_tasks("By Creation", "Ascending")

add_new_task()