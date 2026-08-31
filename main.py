print("Warehouse-Authorization-Project")

#list of employees
employees = [
    {
        "ID": 1,
        "name": "Ryan",
        "status": "Active",
        "role": "General Manager",
        "allowed_entrances": [
            "Frontend",
            "Backend",
            "Reception door",
            "Elevator door",
            "Elevator buttons",
            "Merge door"
        ],
        "areas": [
            "Storage room",
            "Server room",
            "Managers Office",
            "Offloading area",
            "Onloading area",
        ]
    },
    {
        "ID": 2,
        "name": "John",
        "status": "Active",
        "role": "Operations Manager",
        "allowed_entrances": [
            "Backend",
            "Merge door",
            "Elevator door",
            "Elevator buttons",
            "Reception door"
        ],
        "areas": [
            "Offices",
            "Storage room",
            "Security room",
            "Offloading area",
            "Onloading area",
        ]
    },
    {
        "ID": 3,
        "name": "Sophia",
        "status": "Active",
        "role": "Frontend Manager",
        "allowed_entrances": [
            "Frontend",
            "Merge door",
            "Elevator door",
            "Elevator buttons",
            "Reception door"
        ],
        "areas": [
            "Offices",
            "Storage room",
        ]
    },
    {
        "ID": 4,
        "name": "Richie",
        "status": "Active",
        "role": "IT",
        "allowed_entrances": [
            "Frontend",
            "Merge door",
            "Elevator door",
            "Elevator buttons",
            "Reception door"
        ],
        "areas": [
            "Server room",
            "Offices",
        ],
    },
    {
        "ID": 5,
        "name": "Jacob",
        "status": "Active",
        "role": "Security",
        "allowed_entrances": [
            "Backend",
        ],
        "areas": [
            "Security room",
        ]
    },
    {
        "ID": 6,
        "name": "Emily",
        "status": "Active",
        "role": "Customer Support",
        "allowed_entrances": [
            "Frontend",
            "Elevator door",
            "Elevator buttons",
            "Reception door"
        ],
        "areas": [
            "Offices",
        ]
    },
    {
        "ID": 7,
        "name": "Josh",
        "status": "Active",
        "role": "Secretary",
        "allowed_entrances": [
            "Frontend",
            "Elevator door",
            "Elevator buttons",
            "Reception door"
        ],
        "areas": [
            "Offices",
        ]
    },
    {
        "ID": 8,
        "name": "Mia",
        "status": "Active",
        "role": "Supervisor",
        "allowed_entrances": [
            "Frontend",
            "Backend",
            "Elevator door",
            "Elevator buttons",
            "Reception door"
        ],
        "areas": [
            "Offices",
            "Offloading area",
            "Onloading area",
        ]
    },
    {
        "ID": 9,
        "name": "Hector",
        "status": "Active",
        "role": "Janitor",
        "allowed_entrances": [
            "Frontend",
            "Backend",
            "Elevator door",
            "Elevator buttons",
            "Reception door"
        ],
        "areas": [
            "Offices",
            "Storage room",
            "Offloading area",
            "Onloading area",
        ]
    },
    {
        "ID": 10,
        "name": "Maria",
        "status": "Active",
        "role": "Associate",
        "allowed_entrances": [
            "Backend",
        ],
        "areas": [
            "Onloading area",
        ]
    },
    {
        "ID": 11,
        "name": "Steven",
        "status": "Active",
        "role": "Janitor",
        "allowed_entrances": [
            "Backend"
        ],
        "areas": [
            "Offloading area",
            "Onloading area",
        ]
    },
    {
        "ID": 12,
        "name": "Olivia",
        "status": "Inactive",
        "role": "Associate",
        "allowed_entrances": [
            "Backend",
        ],
        "areas": [
            "Offloading area",
        ]
    },
    {
        "ID": 13,
        "name": "Rebecca",
        "status": "Active",
        "role": "Maintenance",
        "allowed_entrances": [
            "Backend",
            "Frontend",
            "Elevator door",
            "Elevator buttons",
            "Reception door"
        ],
        "areas": [
            "Storage room",
            "Electrical room",
            "Offices",
        ]
    },
    {
        "ID": 14,
        "name": "James",
        "status": "Active",
        "role": "Associate",
        "allowed_entrances": [
            "Backend",
        ],
        "areas": [
            "Onloading area",
        ]
    }
]

#1 originally an employee search by ID

#2 Made it into a 'sign in as employee' program

#3 A Base authorization program for the warehouse.

#Currently Updated library making the location traversable throughout the warehouse.

employee_id = int(input("Enter employee ID: "))

employee_exists = False
current_employee = None

for employee in employees:
    if employee["ID"] == employee_id:
        employee_exists = True
        print(employee)
        if employee["status"] == "Inactive":
            print(employee['name'] + " is inactive.")
        else:
            current_employee = employee
            print("Welcome, " + current_employee['name'] + ".")
    else:
        continue
    requested_area = input("Where would you like to go? ")
    if requested_area in current_employee["areas"]:
        print("Entering..." + requested_area)
    else:
        print("Cannot access " + requested_area + ".")


if employee_exists == False:
    print("Employee does not exist.")
