This project is being made because I always thought that being able to change things in the physical world 
through technology was fascinating. This is not anything like that, but the concept of access control and 
authorization could be an interesting idea, and I currently work at a warehouse and thought it would be fun
to make my own interpretation of how access control should be used for each worker based on their role or 
responsibilities in the company. This project will follow the principle that employees only have access to 
the needed areas to perform their jobs successfully.
------------------------------------------------------------------------------------------------------------
It has been a while since I've coded Python, so I've been relearning a lot of concepts while working on this 
and remembered how much I struggle with concepts, looking up how inputs work and how to program simple things 
like looking up a name with a for loop and if statements. The if statements were tricky, especially when it 
came to adding them with true and false logic while figuring out the difference between == and =. I didn't 
start this project to relearn Python but to program my own authorization engine, but it looks like I do need 
to relearn from the ground up.
-------------------------------------------------------------------------------------------------------------
I feel like my progression is getting faster now that I'm understanding the concept more for Python. I went 
from a basic input search for employees by ID to being able to authorise employees to locations in a very 
basic sense. I'll expand on that more and eventually have the floor be something that has to be entered if it 
is based on the current floor the employee is at from the areas available from the floor they currently are 
at. The concept is what is driving me to understand and seek more of what I need to understand to see how far 
I can bring this project all together. I did struggle a bit with the syntax and spacing when dealing with the 
engine, and there was a lot of confusion with parent-child relationships with the variables, but it all 
started to make sense, and more of it keeps coming to me faster as I go.
-------------------------------------------------------------------------------------------------------------
Restructuring the library was a lot more difficult than I thought it would be when I started today. I had to 
change the use of [] since it wasn't a normal list but instead {} to use it as a way for there to be order 
with certain areas and entrances inside the warehouse. I had to change how the concept works and make a new 
library for entrances for employees to eventually be able to move eventually inside the engine, which I will 
eventually have to restructure how the engine works as well. Coding the elevators was confusing at first, but 
then once I thought about it conceptually, the elevators made more sense on how they should function based on 
entrance. It was weird having to put smaller areas that were just a simple room since they didn't lead 
anywhere, but I made that to help with the engine when I add the previous location function into the engine. 
I added a starting location before adding more to the functionality in main.py. The starting location 
definition will give good footing when restructuring how employees will move around the building. It was a 
tedious task to get all the renaming back on every employee, but it helped me understand conceptually how the 
restrictions should work by adding allowed entrance and not only areas determine the employees authorization.
-------------------------------------------------------------------------------------------------------------
Going deeper into access control logic is starting to show difficulty. It started showing when I was 
configuring how the elevators work, which was no easy task. The movement logic had to be restructured based 
on how the elevators work, but the logic behind the access control went further because once the elevator is 
accessed, the employees get to control where they go from there, so if they have access to the elevator, they 
have access to all floors and not to the one they are assigned to. I'm thinking of adding a key for access 
after pressing the button for now or maybe some sort of badge function instead since badges are more realistic
than each employee having a key for each room they need to access.
-------------------------------------------------------------------------------------------------------------
Going deeper into access control logic is starting to show difficulty. Making a leave option along with 
allowing being inside a room that doesn't give other "new" entrances is the next new task, but the issue I'm 
having is being able to leave means there has to be a past location that needs to be known as a variable for 
the employees to leave a room with no other entrances since doors aren't being considered entrances; only 
entrances are defined when there are other entrances to be accessed. It took me a while to understand that 
using a "not in" would be needed to make the engine understand that not only what is inside the entrance guide
is needed, but also being able to enter an area and allowing it based off of restrictions as well. This all 
tied into how the leave function worked since current_area started to get tied into last_area. I put a print 
line under one of the assignment values that gave me a bug, but I figured it out pretty quickly based on the 
terminal output.