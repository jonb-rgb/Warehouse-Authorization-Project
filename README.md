Overview-
This is a Python-based Warehouse simulator built to make an authorization engine the main topic for how access control would work in a real-world environment of a warehouse. This engine shows how, based on employee responsibilities, they are allowed and restricted in the areas of the warhouse. 

I made this simulator to brush up on Python because I find it fascinating that technology can have real-world implications for the physical world. Not only does this help me get better at Python, but it also allows me to better understand why employees have certain permissions.


Project Goals-
The goal of this project is to be able to keep a clean system flowing, allowing people to be where they are supposed to be without having to worry about someone being where they aren't supposed to be. 

This engine is able to show how there is employee-specific authorization with physical access restrictions.

Having a function authorization engine working throughout the whole building.


Current Features-
-Being able to access the building from the outside using the ID from the main code file, you can choose any that has an active status to enter the building.

-There is an elevator that works for those that have access to the second floor and beyond.

-You can go from the frontend to the backend of the warehouse in the lobby.

-The system tracks where you are as you move through the building.

-Authorized employees can access elevator using elevator buttons to navigate between floors.

-Access shows that employees are denied when attempting to enter a location based on authorization.

-Employees remain logged in until they choose to log out from anywhere.


Access Control Design-
-First is there status check; if they are active, they may come in, if it is inactive, they are denied and stay outside the building.

-Second is employees having the proper 'allowed_entrances' to go through entrances

-Next would be if they are allowed in 'areas' because the room and entrances are considered different permissions.

-Traveling is based on 'current_area', 'last_area'(for leaving a room), and 'Entrance_guide' (for lobby areas and the elevator function where there are several options for entrances).


Project Structure-
The 'main.py' will have the authorization engine, employee data, and the engine to explore around the building based on the employee you are logged in as.

'Warehouse_info' is the library for 'Entrance_guide', 'Starting_Location', 'Entrances, 'Warehouse_Floors', and 'roles'.


Running the program-
Type 'py main.py' in the terminal.

Enter ID when prompted.

Navigate and test the permissions of the employee in the building.

Type 'Logout' when finished.

When you originally run 'main.py' there will be a prompt for a login ID, that is where the ID numbers in 'main.py' will be useful where the employee data is. 

There are currently 1-14 IDs for different employees with different roles, entrance permissions, area permissions, and statuses. 

Under the employee information, it shows what areas they are allowed along with if they are able to use the elevators or not. 

You may enter rooms, but you can't do anything else except to leave the room and keep exploring the building.

You can log out and see other permissions of another employee.


Future plans-
-audit log
I'd like to have a list of people who have accessed certain areas like a long session outside of logging in to show different people working around the area.

-more clear denial reason
Giving clear denial reasons shows the user why they can't access an area

-more detailed permissions
More detailed permissions means the authorization system becomes more smarter and possibly more dynamic

Jounral-
There is a journal that talks about what I did and the problems I faced making this engine along with a more detailed reason as to why I made this engine.
[Read the journal](Journal.md)