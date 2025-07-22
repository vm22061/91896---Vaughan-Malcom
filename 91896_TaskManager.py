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
        "Tasks assigned" : ["T2","T1"],
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

task_edit_or_add_value_sets = {
    "Assignee" : ["JSM","JLO","BDI"],
    "Priority" : [3,2,1],
    "Status" : ["Complete","In Progress","Blocked","Not Started"]
}

def add_new_task():
    """"Using this function, the users will be able to add a new task to the 
        task list, assign a team member, priority status and discription"""

    edit_or_add_multenterbox([],"Add a new task",None)

def edit_or_add_multenterbox(initial_values,title,edit_or_add):
    """"IDK"""

    prompt = "Please enter the desired information below..."
    entering_fields = []

    for dictionary_definitions in task_dictionary.values():
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

    for value in preassigned_values:
        task_details.append("")

    if edit_or_add == None:
        preassigned_value_choiceboxes([],-1,edit_or_add,task_details,title)
    else:
        preassigned_preselects = []
        preassigned_preselects.append(task_dictionary[edit_or_add]["Assignee"])
        preassigned_preselects.append(task_dictionary[edit_or_add]["Priority"])
        preassigned_preselects.append(task_dictionary[edit_or_add]["Status"])
        preassigned_value_choiceboxes(preassigned_preselects,-1,edit_or_add,
        task_details,title)

def preassigned_value_choiceboxes(preselects,repeat_iteration,edit_or_add,
task_details,title):
    """ENTER HERE"""

    choicebox_choices = [""]
    choicebox_preselect = []

    repeat_iteration += 1

    if repeat_iteration > 2:
        if edit_or_add == None:
            task_dictionary[f"T{int(len(task_dictionary))+1}"] = {
                "Title" : task_details[0],
                "Description" : task_details[1],
                "Assignee" : task_details[2],
                "Priority" : task_details[3],
                "Status" : task_details[4]
                }
            for member in team_member_dictionary:
                if member == task_details[2]:
                    print(list( \
                        team_member_dictionary[member]["Tasks assigned"]))
                    if [f"T{int(len(task_dictionary))}"] not in \
                        list(team_member_dictionary[member]["Tasks assigned"]):
                        print(f"T{int(len(task_dictionary))}")
                        team_member_dictionary[member]["Tasks assigned" \
                            ].append(f"T{int(len(task_dictionary))}")
                        team_member_dictionary[member]["Tasks assigned"].sort()
                        print(list(team_member_dictionary[member][ \
                            "Tasks assigned"]))
            easygui.msgbox("A new task has been successfully added! \
                \n\nReturning to main menu...")
            main_menu()
        else:
            task_dictionary[edit_or_add] = {
                "Title" : task_details[0],
                "Description" : task_details[1],
                "Assignee" : task_details[2],
                "Priority" : task_details[3],
                "Status" : task_details[4]
                }
            easygui.msgbox(f"Task {edit_or_add} has been successsfully \
                updated!\n\nReturning to main menu...")
            main_menu()

    if repeat_iteration != 1:
        choicebox_subject = preassigned_values[repeat_iteration]
        choicebox_prompt = f"Set the task's {choicebox_subject}..."
        choicebox_title = f"Set task's {choicebox_subject}"
        choicebox_choices = task_edit_or_add_value_sets[choicebox_subject]

        if (choicebox_subject == "Assignee")\
            and not ("Next step" in choicebox_choices):
            choicebox_choices.append("Next step")

        if not ("Return to previous step" in choicebox_choices):
            choicebox_choices.append("Return to previous step")
        if not ("Return to main menu" in choicebox_choices):
            choicebox_choices.append("Return to main menu")

        if preselects != []:
            choicebox_preselect = [preselects][repeat_iteration]


    if repeat_iteration == 1:
        selected_value = priority_integerbox()
    else:
        selected_value = easygui.choicebox(choicebox_prompt,choicebox_title,
        choicebox_choices,choicebox_preselect)

    if selected_value == None:
        main_menu()
    elif selected_value == "Next step":
        preassigned_value_choiceboxes(preselects,repeat_iteration,edit_or_add,
        task_details,title)
    elif selected_value == "Return to previous step":
        if repeat_iteration == 0:
            edit_or_add_multenterbox(task_details,title,edit_or_add)
        else:
            preassigned_value_choiceboxes(preselects,int(repeat_iteration)-2,
            edit_or_add,task_details,title)
    elif selected_value == "Return to main menu":
        main_menu()
    elif repeat_iteration == 0:
        task_details[2] = selected_value
        preassigned_value_choiceboxes(preselects,repeat_iteration,
            edit_or_add,task_details,title)
    elif repeat_iteration == 1:
        task_details[3] = selected_value
        preassigned_value_choiceboxes(preselects,repeat_iteration,
            edit_or_add,task_details,title)
    elif repeat_iteration == 2:
        task_details[4] = selected_value
        preassigned_value_choiceboxes(preselects,repeat_iteration,
            edit_or_add,task_details,title)

def priority_integerbox():

    upper = task_edit_or_add_value_sets["Priority"][0]
    lower = task_edit_or_add_value_sets["Priority"][-1]
    msg = f"Enter priority from {upper} (high priority) to {lower} "
    msg += "(low priority)\n\n[ Press 'Exit' to return to previous step ]"

    selected_value = easygui.integerbox(msg,"Task priority",lowerbound=lower, upperbound=upper)

    if selected_value == None:
        selected_value = "Return to previous step"

    print(selected_value)

    return selected_value

#def update_task():

#def search():

def generate_report():

    report_text = ["Task report:"]
    status_list = []
    amount_of_status_list = []

    for status in task_edit_or_add_value_sets["Status"]:
        status_list.append(status)
        amount_of_status_list.append(0)

    print(status_list)
    print(amount_of_status_list)

    for task in task_dictionary:
        repeat_iteration = -1
        for status in status_list:
            repeat_iteration += 1
            if task_dictionary[task]['Status'] == status_list[int(repeat_iteration)]:
                print(f"value : {amount_of_status_list[repeat_iteration]}")
                amount_of_status_list[int(repeat_iteration)] = int(amount_of_status_list[int(repeat_iteration)]) + 1

    repeat_iteration = -1
    
    for status in status_list:
        repeat_iteration += 1  
        report_text.append(f"\n[ {status} ] : {amount_of_status_list[repeat_iteration]}")

    exit = easygui.msgbox("\n".join(report_text),"Generated task report")

    if exit == None:
        main_menu()
    else:
        main_menu()

def print_tasks():

    choicebox_text = ["Current tasks"]

    for task_id, task_details in task_dictionary.items():
        choicebox_text.append(f"\n[ {task_dictionary[task_id]['Title']} ]")
        for task_key, task_value in task_details.items():
            if task_key != "Title":
                choicebox_text.append(f"\t{task_key}: {task_value}")
    
    exit = easygui.msgbox("\n".join(choicebox_text),"Print tasks")

    if exit == None:
        main_menu()
    else:
        main_menu()

def main_menu():

    navgation_choices = ["Add new task","Update task", \
        "Search for task or team member","Generate report","Task summary"]

    main_menu_navigation = easygui.buttonbox("Main navigation:", \
        "Main menu",navgation_choices)

    if main_menu_navigation == navgation_choices[0]:
        add_new_task()
    elif main_menu_navigation == navgation_choices[1]:
        main_menu()
    elif main_menu_navigation == navgation_choices[2]:
        easygui.integerbox("")
    elif main_menu_navigation == navgation_choices[3]:
        generate_report()
    elif main_menu_navigation == navgation_choices[4]:
        print_tasks()

main_menu()