#exercise 7.5
"""
pw = input("Enter your password")
if pw == "secret":
	print("welcome to the matrix")
ice_creams = int(input("input how many ice creams's you would like"))
if ice_creams > 20:  
  print("we do not have the stock for this amount of ice cream's")
elif ice_creams <= 20: 
 print("ok your order is being processed")
user_miles = int(input("how far are you traveling user in km"))
if user_miles > 200:
	print("please fill up your car with gasoline")
elif user_miles <= 200:
	print("you have enough gas to travel to your location")
user_age = int(input("how old are you"))
if user_age >= 18:
	print("you are now an adult")
elif user_age < 18:
	print("you are still considered a minor")
user_movie = input("what is your favorite movie")
if user_movie == "lord of the rings":
 print("you have great taste")
elif user_movie != "lord of the rings":
 print("lord of the rings is the better movie")
 
tale = input("have you heard of the tale of darth plagueis the wise")
if tale == "yes":
 print("you are a nerd")
else:
	print("look up the tale of darth plagueis")
director = input("who directed Passion of the Christ")
if director == "mel gibson":
	print("correct")
elif director =="MEL GIBSON":
	print("correct")
elif director == "Mel Gibson":
	print("correct")
else: 
	print("Mel Gibson did")
"""

score = 0
 
movie = input("what is my favorite movie")
if movie == "jigsaw":
 score = (score + 1)
else: 
 print("jigsaw is my favorite movie no point")
print(f"{score}")
book = input("what is my favorite book")
if book == "nothing":
 print("your right")
 score = (score + 1)
else: 
 print("if you put a book then you dont know me well")
print(f"{score}")
game = input("what is one of my favorite games")
if game == "halo" or "apex legends":
 print("yes that is correct")
 score = (score + 1)
elif score != "halo" or "apex legends":
 print("you are wrong")
print(f"{score}")
subject = input("what is my favorite subject")
if subject == "maths":
 print("you are correct")
 score = (score + 1)
else:
 print("mmm nah wrong answer")
print(f"{score}")
console = input("what is my favorite console brand")
if console == "xbox":
 print("correct")
 score = (score + 1)
elif console == "playstation":
 print("your wrong")
 score = (score - 1)
 print(f"{score}")
 if score < 5:
 	print("you fail my test")
if score ==5:
 print("you have passed this time")
 