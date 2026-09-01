Starting_Location = "Outside"

Warehouse_floors = {
    1: [
        "Lobby",
        "Main Area",
        "Storage room",
        "Security room",
        "Elevator",
        "Offloading area",
        "Onloading area",
    ],
    2: [
        "Offices",
        "Managers Office",
        "Reception Lobby",
        "Elevator",
        "2nd Floor Lobby",
    ],
    3: [
        "Server room",
        "Electrical room",
        "Elevator",
        "3rd Floor Lobby",
    ]
}

Entrances = [
    "Frontend",
    "Backend",
    "Merge door",
    "Reception door",
    "Elevator door",
]

Entrance_guide = {
    "Outside": {
        "Frontend": "Lobby",
        "Backend": "Main Area",
    },
    "Lobby": {
        "Merge door": "Main Area",
        "Elevator door": "Elevator",
        "Storage room": "Storage room",
    },
    "Main Area": {
        "Merge door": "Lobby",
        "Security room": "Security room",
    },
    "Elevator": {
        "Elevator buttons": {
            "First floor": "Lobby",
            "Second floor": "2nd Floor Lobby",
            "Third floor": "3rd Floor Lobby",
        }
    },
    "2nd Floor Lobby": {
        "Elevator door": "Elevator",
        "Reception door": "Reception Lobby",
    },
    "Reception Lobby": {
        "Reception door": "2nd Floor Lobby",
        "Offices": "Offices",
        "Managers Office": "Managers Office",
    },
    "3rd Floor Lobby": {
        "Elevator door": "Elevator",
        "Server room": "Server room",
        "Electrical room": "Electrical room",
    }
}

roles = [
    "Associate",
    "Janitor",
    "Supervisor",
    "Secretary",
    "Customer Support",
    "Security",
    "Maintenance",
    "IT",
    "Frontend Manager",
    "Operations Manager",
    "General Manager",
]
