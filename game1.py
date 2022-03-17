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
current_room = space

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
 global current_room
if current_room is not space:
	say("there is no airlock here")
else:
	current_room = spaceship
	print("""you heave yourself into the spaceship and
	slam you hand on the button to close the door.
	""")
	print(current_room)

cargo = "Room1"
@when("enter cargo")
@when("enter storage")
@when("enter cargo hold")
def enter_cargo():
 global current_room
if current_room == space:
	print("cannot enter cargo please enter airlock to proceed")
elif current_room == spaceship:
	print("""you enter the storage area of your ship
	your foot steps echo as you enter the room""")



def main():
	start()

if __name__ == '__main__':
	main()