from adventurelib import *

space = Room("""
	you are drifting in space it feels very cold.
	a slate-blue spaceship sits completely silently to your left,
	its airlock open and waiting.
	""")

spaceship = Room("""
	The bridge if the spaceship is shiny and white, with thousands
	 of small, red, blinking lights
	""")

cargo = Room("""
	The storage of your ship
	""")
hallway = Room("""a short distance to travel between locations
""")
docking = ("""this is where the ships come and land
""")
bridge = ("""the commanding location of the ship
""")
quarters = ("""the sleeping quarters of the ship
""")
mess_hall = ("""entering quarters of the ship
""")
escape_pods = ("""used as a last resort the escape pods are located here
""")
current_room = space
print(current_room)

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global current_room
	if current_room is not space:
		say("there is no airlock here")
	else:
		current_room = spaceship
		say("you heave yourself into the ship")
		print(current_room)
@when("enter hallway")
@when("enter hall")
@when("enter passage")
def enter_hallway():
	global current_room
	if current_room is not spaceship:
		say("you need to be in the airlock to use this passage")
	else:
		current_room = hallway
		say("you enter the passage from the airlock there is a sign here\n it reads cargo bridge mess_hall")
@when("enter cargo")
@when("enter storage")
def enter_cargo():
	global current_room
	if current_room is not hallway:
		say("you need to check out the hallway before you go to storage")
	else:
		current_room = cargo 
		say("you walk into the storage it is cold here but it is also massive")







def main():
	start()

if __name__ == '__main__':
	main()