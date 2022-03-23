from adventurelib import *
#rooms
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
#define connections
spaceship.east = hallway
spaceship.south = quarters
hallway.east = bridge
hallway.north = cargo
hallway.south = mess_hall
quarters.east = mess_hall 
bridge.south = escape_pods
cargo.east = docking
current_room = space
print(current_room)
@when ("go DIRECTION")
def travel(derections):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exits(direction)
		print(f"you go {direction}.")
		print(current_room)
		print(current_room.exits())
	else:
		print("you cant go that way")

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



def main():
	start()

if __name__ == '__main__':
	main()