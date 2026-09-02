from Warehouse_info import Entrance_guide, Starting_Location


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
            "Backend",
        ],
        "areas": [
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
            "Reception door",
            "Merge door"
        ],
        "areas": [
            "Lobby",
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
            "Reception door",
            "Merge door"
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

#4 Updated library making the location traversable throughout the warehouse.

#5 Made the elevator functional while restructuring how the logging in works.

#6 Made a leave function along with being able to enter different areas with no other entrances.

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
            current_area = Starting_Location
            last_area = None

            while current_employee != None:
                print("Welcome, " + current_employee['name'] + ".")
                print("Current location: ", current_area)

                if current_area in Entrance_guide:
                    print("Available entrances: ")

                    for entrance in Entrance_guide[current_area]:
                        print(entrance)   

                else:
                    print("Available actions: ")
                    print("Leave")

                if current_area not in Entrance_guide:
                    requested_access = input("Leave room?")

                    if requested_access == "Leave":
                        print("Leaving " + current_area + "...")
                        current_area = last_area
                        continue
                
                current_entrances = current_employee["allowed_entrances"]

                requested_access = input("Which entrance would you like to use? ")

                if requested_access == "Logout":
                    current_employee = None
                    print("Logging out...")

                elif current_area == "Elevator" and requested_access == "Elevator buttons":
                    floor_options = Entrance_guide[current_area]["Elevator buttons"]

                    for floor in floor_options:
                        print(floor)
                    floor_choice = input("Which floor would you like to go to? ")

                    if floor_choice in floor_options:
                        current_area = floor_options[floor_choice]
                        print("Heading to " + current_area + "...")

                elif requested_access in current_entrances:
                    print("Going through " + requested_access + "..." )
                    current_area = Entrance_guide[current_area][requested_access]

                elif requested_access in current_employee["areas"]:
                    last_area = current_area
                    current_area = Entrance_guide[current_area][requested_access]
                    print("Entering " + current_area + "...")

                else:
                    print("Access denied for " + requested_access + ".")
    else:
        continue

if employee_exists == False:
    print("Employee does not exist.")
