import easygui

task_dictionary = {
    "T1" : {
        "title" : "Design Homepage",
        "description" : "Create a mockup of the homepage",
        "assignee" : "JSM",
        "priority" : 3,
        "status" : "In Progress"
    },
    "T2" : {
        "title" : "Implement Login page",
        "description" : "Create the Login page for the website",
        "assignee" : "JSM",
        "priority" : 3,
        "status" : "Blocked"
    },
    "T3" : {
        "title" : "Fix navigation menu",
        "description" : "Fix the navigation menu to be more user-friendly",
        "assignee" : "", #"None"???
        "priority" : 1,
        "status" : "Not Started"
    },
    "T4" : {
        "title" : "Add payment processing",
        "description" : "Implement payment processing for the website",
        "assignee" : "JLO",
        "priority" : 2,
        "status" : "In Progress"
    },
    "T5" : {
        "title" : "Create an About Us page",
        "description" : "Create a page with information about the company",
        "assignee" : "BDI",
        "priority" : 1,
        "status" : "Blocked"
    }
}

team_member_dictionary = {
    "JSM" : {
        "name" : "John Smith",
        "email" : "John@techvision.com",
        "tasks_assigned" : "John Smith",
    }
}
