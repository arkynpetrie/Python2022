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
		say("you enter the passage from the airlock")
@when("enter cargo")









def main():
	start()

if __name__ == '__main__':
	main()