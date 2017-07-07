start = '''
You're walkin down an alley one night, and you're kidnapped. The person who kidnapped threw you
into the lake. When you finally woke up, you were in the rainforest.
You were stranded with no people, food, or water
'''


print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("As you turn left, you see a dark shadow and walk towards to it. Then you realize your stepping on a big dinousaur footprint. You feel like someone's watching every step you take, and as soon as you turn around, the dinousaur is right in front of your face. Do you run or fight the dinousaur?") # finished the story by writing what happens
    user_input = input()
    if user_input == "run":
        print("Out of terror you began to run, as you run with all the speed from your body, you realize there's no other way out and fall off a cliff.")
    #user_input = input()
    if user_input == "fight":
        print("You win!")
if user_input == "right":
    print("You come across a beautiful luxorious bridge. Find food by an old creepy lady. Do you starve to death or eat the poisonous food?")
    user_input = input()
    if user_input == "starve to death":
        print("A nearby helicopter rescues you and saves your life!")
    #user_input = input()
    if user_input == "eat the poisonous food":
        print("You die!")
