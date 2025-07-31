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
        "Assignee" : "",
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

task_edit_or_add_value_sets = {
    "Assignee" : ["JSM","JLO","BDI"],
    "Assignee Choices" : ["JSM : John Smith","JLO : Jane Love",
    "BDI : Bob Dillon"],
    "Priority" : [3,2,1],
    "Status" : ["Complete","In Progress","Blocked","Not Started"]
}

assignee_list_length = len(task_edit_or_add_value_sets["Assignee"])

status_list = []

for status in task_edit_or_add_value_sets["Status"]:
    status_list.append(status)

def add_new_task():
    """Using this function, the users will be able to add a new task to 
    the task list, assign a team member, priority, status and 
    discription"""

    edit_or_add_multenterbox([],"Add a new task",None)

def edit_or_add_multenterbox(initial_values,title,edit_or_add):
    """Within this function holds the code to generate a multenterbox 
    for users to input both the title and description of a task"""

    prompt = "Please enter the desired information below..."
    entering_fields = []

    # Gets all of the values for users to enter in that aren't 
    # "Assignee", "Priority" or "Status."
    for dictionary_definitions in task_dictionary.values():
        for dictionary_key in dictionary_definitions:
            if dictionary_key not in entering_fields:
                if dictionary_key not in preassigned_values:
                    entering_fields.append(dictionary_key)     

    # Generates the multenterbox.
    task_details = easygui.multenterbox(prompt,title,entering_fields,
        initial_values)

    # When the user presses 'Cancel' they are sent to either the main 
    # menu or the update task choice choicebox.
    if task_details == None:
        if edit_or_add == None:
            main_menu()
        else:
            update_task()
    
    # Checks if any of the fields are empty and if so displays an error 
    # message. 
    for entering in task_details:
        if entering == '':
            easygui.msgbox("Please fill in all fields...")
            edit_or_add_multenterbox(task_details,title,edit_or_add)

    # Gets a string of empty values equal to the length of the 
    # preassigned value list.
    for value in preassigned_values:
        task_details.append("")

    # Checks whether the user is adding or editting a the task and 
    # enters the next steps in the choice/integerboxes.
    if edit_or_add == None:
        preassigned_value_choiceboxes([],-1,edit_or_add,task_details,title)    
    else:

        # if the user is editing this sets the preselected values for 
        # the remaining steps.
        preassigned_preselects = []

        # Gets the index value of the preselected assignee choice.
        assingee_preselect = -1
        if task_dictionary[edit_or_add]["Assignee"] != '':
            for assingee in task_edit_or_add_value_sets["Assignee"]:
                assingee_preselect += 1
                if assingee == task_dictionary[edit_or_add]["Assignee"]:
                    preassigned_preselects.append(assingee_preselect)
        elif task_dictionary[edit_or_add]["Assignee"] == "":
                preassigned_preselects.append(assignee_list_length)

        # Gets preexisting value for the task's priority.
        preassigned_preselects.append(task_dictionary[edit_or_add]["Priority"])

        # Gets the index value of the preselected status choice.
        status_preselect = -1
        for status in task_edit_or_add_value_sets["Status"]:
            status_preselect += 1
            if status == task_dictionary[edit_or_add]["Status"]:
                preassigned_preselects.append(status_preselect)
        preassigned_value_choiceboxes(preassigned_preselects,-1,edit_or_add,
        task_details,title)

def preassigned_value_choiceboxes(preselects,repeat_iteration,edit_or_add,
task_details,title):
    """ENTER HERE"""

    choicebox_choices = [""]
    choicebox_preselect = []

    # Gains 1 each time this function is run so it knows when to stop 
    # and get all the task's information.
    repeat_iteration += 1

    # Checks if it's on its last repeat and if so sets the tasks new 
    # deatils.
    if repeat_iteration > 2:

        # Checks if the user is editing or adding a new task.
        if edit_or_add == None:

            # If adding a new task it gets a new id and dictionary
            # values.
            task_dictionary[f"T{int(len(task_dictionary))+1}"] = {
                "Title" : task_details[0],
                "Description" : task_details[1],
                "Assignee" : task_details[2],
                "Priority" : task_details[3],
                "Status" : task_details[4]
                }
            
            # Adds the task to the chosen team members "Tasks assigned" 
            # list if the status isn't "Complete."
            if task_details[4] != "Complete":
                for member in team_member_dictionary:
                    if member == task_details[2]:
                        if [f"T{int(len(task_dictionary))}"] not in \
                            list(team_member_dictionary[member
                            ]["Tasks assigned"]):
                            team_member_dictionary[member]["Tasks assigned" \
                                ].append(f"T{int(len(task_dictionary))}")
                            team_member_dictionary[member
                            ]["Tasks assigned"].sort()

            # Gets the tasks information in a readible format for a 
            # preview at the end of the process.
            task_format = []

            for task_id, task_values in task_dictionary.items():
                task_title = task_dictionary[task_id]['Title']
                if task_dictionary[task_id]["Title"] == task_details[0]:
                    task_format.append(
                        f"\n[ {task_id} : {task_title} ]")
                    for task_key, task_value in task_values.items():
                        if task_key != "Title":
                            task_format.append(f"\t{task_key}: {task_value}")

            task_format = "\n".join(task_format)

            # Displays a msgbox with a success message and a preview of 
            # the added task.
            msg = "A new task has been successfully added!\n"
            msg += task_format
            msg += "\n\nReturning to main menu..."
            easygui.msgbox(msg)

            # Returns the user to the main menu once they press "OK."
            main_menu()

        else:

            # This runs if the user is editting the task to compair the 
            # input information to the preexisting information.
            if task_dictionary[edit_or_add]["Assignee"] != task_details[2]:
                # If the task was changed the new choice is added to the 
                # chosen assignees tasks assigned list and taken away 
                # from the previous assignee.
                for member_id in team_member_dictionary:
                    if member_id == task_details[2]:
                        tasks_assigned = \
                            team_member_dictionary[member_id]["Tasks assigned"]
                        if edit_or_add not in tasks_assigned:
                            tasks_assigned.append(edit_or_add)
                            tasks_assigned.sort()
                            team_member_dictionary[
                                member_id]["Tasks assigned"] = tasks_assigned
                    if task_dictionary[edit_or_add]["Assignee"] == member_id:
                        new_task_list = []
                        for set_task in team_member_dictionary[member_id]["Tasks assigned"]:
                            if set_task != edit_or_add:
                                new_task_list.append(set_task)
                        team_member_dictionary[member_id]["Tasks assigned"] = \
                            new_task_list

            if task_details[4] == "Complete":
                for members in team_member_dictionary:
                    if members == task_details[2]:
                        new_task_list = []
                        for set_task in \
                            team_member_dictionary[members]["Tasks assigned"]:
                            if set_task != edit_or_add:
                                new_task_list.append(set_task)
                        team_member_dictionary[members]["Tasks assigned"] = \
                            new_task_list

            task_dictionary[edit_or_add] = {
                "Title" : task_details[0],
                "Description" : task_details[1],
                "Assignee" : task_details[2],
                "Priority" : task_details[3],
                "Status" : task_details[4]
                }
            
            task_format = []

            for task_id, task_values in task_dictionary.items():
                task_name = task_dictionary[task_id]['Title']
                if task_dictionary[task_id]["Title"] == task_details[0]:
                    task_format.append(f"\n[ {task_id} : {task_name} ]")
                    for task_key, task_value in task_values.items():
                        if task_key != "Title":
                            task_format.append(f"\t{task_key}: {task_value}")
            
            task_format = "\n".join(task_format)
            message = "Task "
            message += edit_or_add
            message += " has been successsfully updated!\n"
            message += task_format
            message += "\n\nReturning to main menu..."

            easygui.msgbox(message)
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
        choicebox_preselect = preselects[repeat_iteration]


    if repeat_iteration == 1:
        selected_value = priority_integerbox(choicebox_preselect)
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
    else:
        repeat_vlaue = int(repeat_iteration) + 2
        task_details[repeat_vlaue] = selected_value
        preassigned_value_choiceboxes(preselects,repeat_iteration,
            edit_or_add,task_details,title)

def priority_integerbox(choicebox_preselect):

    upper = task_edit_or_add_value_sets["Priority"][0]
    lower = task_edit_or_add_value_sets["Priority"][-1]
    msg = f"Enter priority from {upper} (high priority) to {lower} "
    msg += "(low priority)\n\n[ Press 'Cancel' to return to previous step ]"

    if choicebox_preselect != []:
        selected_value = easygui.integerbox(msg,"Task priority",
        choicebox_preselect,lower,upper)
    else:
        selected_value = easygui.integerbox(msg,"Task priority",
        lowerbound=lower, upperbound=upper)

    if selected_value == None:
        selected_value = "Return to previous step"

    return selected_value

def update_task():

    task_list = []
    
    for task in task_dictionary:
        task_list.append(f'{task} : {task_dictionary[task]["Title"]}')

    task_choice = easygui.choicebox("Which task would you like to update?",
    "Update task",task_list)

    if task_choice == None:
        main_menu()
    else:
        task_chosen = []
        task_multenterbox_details = []
        task_number = -1

        for task in task_list:
            task_number += 1
            if task == task_choice:
                task_chosen = task_number
        repeat_iteration = -1
        for task in task_dictionary:
            repeat_iteration += 1
            if repeat_iteration == task_chosen:
                task_choice = task_dictionary[task]["Title"]
                
        for task in task_dictionary:
            if task_dictionary[task]["Title"] == task_choice:
                task_chosen = task
                task_multenterbox_details.append(
                    task_dictionary[task]["Title"]
                    )
                task_multenterbox_details.append(
                    task_dictionary[task]["Description"]
                    )

        edit_or_add_multenterbox(task_multenterbox_details,"Update task",
        task_chosen)

def search(choice):

    if choice == None:
        task_or_team_member = easygui.buttonbox(
            "Would you like to search for a task or a team member?",
            "Search task or team member",
            ["Search for task", "Search for team member",
            "Return to main menu"])
    else:
        task_or_team_member = choice

    if task_or_team_member == None:
        main_menu()
    if task_or_team_member == "Return to main menu":
        main_menu()
    elif task_or_team_member == "Search for task":

        task_list = []

        for id in task_dictionary:
            task_list.append(f'{id} : {task_dictionary[id]["Title"]}')

        task_choice = easygui.choicebox(
            "Choose a task to access:" + \
                "\n\n(Press 'Cancel' to return to search choice)",
        task_or_team_member,task_list)

        if task_choice == None:
            search(None)
        else:
            task_number = -1
            for task in task_list:
                task_number += 1
                if task == task_choice:
                    task_chosen = task_number
            repeat_iteration = -1
            for task in task_dictionary:
                repeat_iteration += 1
                if repeat_iteration == task_chosen:
                    task_choice = task_dictionary[task]["Title"]

        task_details = []

        for task_id, task_values in task_dictionary.items():
            task_title = task_dictionary[task_id]['Title']
            if task_dictionary[task_id]["Title"] == task_choice:
                task_details.append(f"\n[ {task_id} : {task_title} ]")
                for task_key, task_value in task_values.items():
                    if task_key != "Title":
                        task_details.append(f"\t{task_key}: {task_value}")

        easygui.msgbox("\n".join(task_details),"Task details")

        search("Search for task")

    elif task_or_team_member == "Search for team member":

        member_list = []

        for id in team_member_dictionary:
            member_list.append(f'{id} : {team_member_dictionary[id]["Name"]}')

        member_choice = easygui.choicebox("Choose a team member to access:" + \
                "\n\n(Press 'Cancel' to return to search choice)",
        task_or_team_member,member_list)

        if member_choice == None:
            search(None)
        else:
            member_number = -1
            for member in member_list:
                member_number += 1
                if member == member_choice:
                    member_chosen = member_number
            repeat_iteration = -1
            for member in team_member_dictionary:
                repeat_iteration += 1
                if repeat_iteration == member_chosen:
                    member_choice = team_member_dictionary[member]["Name"]

        member_details = []

        for member_id, member_values in team_member_dictionary.items():
            if team_member_dictionary[member_id]["Name"] == member_choice:
                member_name = team_member_dictionary[member_id]['Name']
                member_details.append(
                    f"\n[ {member_id} : {member_name} ]"
                    )
                for member_key, member_value in member_values.items():
                    if member_key != "Name":
                        if isinstance(member_value, list):
                            member_value_text = ", ".join(member_value)
                            member_details.append(
                                f"\t{member_key}: {member_value_text}"
                                )
                        else:
                            member_details.append(
                                f"\t{member_key}: {member_value}"
                                )
                        
        easygui.msgbox("\n".join(member_details),"team member details")

        search("Search for team member")

def generate_report():

    report_text = ["Task report:"]

    amount_of_statuses = []

    for status in task_edit_or_add_value_sets["Status"]:
        if status not in ["Return to main menu","Next step",
        "Return to previous step"]:
            amount_of_statuses.append(0)

    amount_of_status_list = amount_of_statuses

    for task in task_dictionary:
        repeat_iteration = -1
        for status in status_list:
            repeat_iteration += 1
            if task_dictionary[task]['Status'] == \
                status_list[int(repeat_iteration)]:
                amount_of_status_list[int(repeat_iteration)] = \
                    int(amount_of_status_list[int(repeat_iteration)]) + 1

    repeat_iteration = -1
    
    for status in status_list:
        repeat_iteration += 1  
        report_text.append(
            f"\n[ {status} ] : {amount_of_status_list[repeat_iteration]}"
            )

    exit = easygui.msgbox("\n".join(report_text),"Generated task report")

    if exit == None:
        main_menu()
    else:
        main_menu()

def print_tasks():

    choicebox_text = ["Current tasks"]

    for task_id, task_details in task_dictionary.items():
        task_name = task_dictionary[task_id]['Title']
        choicebox_text.append(f"\n[ {task_id} : {task_name} ]")
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
        update_task()
    elif main_menu_navigation == navgation_choices[2]:
        search(None)
    elif main_menu_navigation == navgation_choices[3]:
        generate_report()
    elif main_menu_navigation == navgation_choices[4]:
        print_tasks()
    else:
        quit()

main_menu()