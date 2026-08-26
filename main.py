print("Warehouse-Authorization-Project")

employees = [
    {
        "ID": 1,
        "name": "Ryan",
        "status": "Active",
        "role": "General Manager",
        "areas": [
            "Frontend",
            "Backend",
            "Offices",
            "Storage",
            "Server Room",
            "Managers Office"
        ]
    },
    {
        "ID": 2,
        "name": "John",
        "status": "Active",
        "role": "Operations Manager",
        "areas": [
            "Frontend",
            "Backend",
            "Offices",
            "Storage"
        ]
    },
    {
        "ID": 3,
        "name": "Sophia",
        "status": "Active",
        "role": "Frontend Manager",
        "areas": [
            "Frontend",
            "Offices",
            "Storage",
            "Server Room"
        ]
    },
    {
        "ID": 4,
        "name": "Richie",
        "status": "Active",
        "role": "IT",
        "areas": [
            "Frontend",
            "Backend",
            "Server Room",
            "Offices"
        ]
    },
    {
        "ID": 5,
        "name": "Jacob",
        "status": "Active",
        "role": "Security",
        "areas": [
            "Backend",
            "Security Room"
        ]
    },
    {
        "ID": 6,
        "name": "Emily",
        "status": "Active",
        "role": "Customer Support",
        "areas": [
            "Frontend",
            "Offices"
        ]
    },
    {
        "ID": 7,
        "name": "Josh",
        "status": "Active",
        "role": "Secretary",
        "areas": [
            "Frontend"
        ]
    },
    {
        "ID": 8,
        "name": "Mia",
        "status": "Active",
        "role": "Supervisor",
        "areas": [
            "Frontend",
            "Backend",
            "Offices"
        ]
    },
    {
        "ID": 9,
        "name": "Hector",
        "status": "Active",
        "role": "Janitor",
        "areas": [
            "Frontend",
            "Backend",
            "Offices",
            "Storage"
        ]
    },
    {
        "ID": 10,
        "name": "Maria",
        "status": "Active",
        "role": "Associate",
        "areas": [
            "Backend"
        ]
    },
    {
        "ID": 11,
        "name": "Steven",
        "status": "Active",
        "role": "Janitor",
        "areas": [
            "Backend"
        ]
    },
    {
        "ID": 12,
        "name": "Olivia",
        "status": "Inactive",
        "role": "Associate",
        "areas": [
            "Backend"
        ]
    }
]

# employee search by ID

employee_id = int(input("Enter employee ID: "))

employee_exists = False

for employee in employees:
    if employee["ID"] == employee_id:
        employee_exists = True
        print(employee)

if employee_exists == False:
    print("Employee does not exist.")