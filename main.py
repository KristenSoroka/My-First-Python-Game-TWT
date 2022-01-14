print("Welcom To My First Python Game!")
#Youtube Tech with Tim https://youtu.be/7R-CfL21zIY
#Choose your own adventure style game

# Goal: make it home alive
# outline:
# 1. North or South:  L- you can move on, R- you die
# 2. Swamp: You will make it to the other side but will lose hearts no matter what.
# 3. A fork in the road: Left to the mountains, right into the woods.  you will either die or make it home!


#greeting
name = input('What is your name? ')
age = int(input('What is your age? '))
print(f'Hello, {name.upper()}! Welcome to your own adventure game! You are {age} years old.')
#health of player
hearts = 10


#age verification using if/elif/else and nested statements
if age >=18:
    print("You are old enough to play!")
    wants_to_play = input('Do you want to play?(yes/no) ').lower()
    
    if wants_to_play == "yes":
        print("Lets Play!")
        print(f"You are starting with {hearts} hearts")
        
        # Left or Right Choice
        left_or_right = input("First choice....Left or Right?(left/right) ").lower()
        
        if left_or_right == "left":
          ans = input("Nice! You followed the path and reached a swamp.  Do you go across or go around?(across/around) ").lower()
          # Across or around the swamp choice
          if ans == "around":
            print("You were attacked by swamp people and lost 5 hearts")
            hearts -= 5
            if hearts > 0:
                print(f"You made it to the other side of the swamp alive. You have {hearts} hearts")
                #mountians v froest
                ans = input("You conintue along the path and find a fork in the road. You can go thru the forest or into the mountains. Where do you go?(forest/mountains) ")
                if ans == "forest":
                    print("You decided to go thru the forest and ate some poisonous berries and lost 5 hearts")
                    hearts -= 5
                    if hearts > 0:
                        print("You made it home alive")
                    else: 
                        print("You died in the forest. You lose!")
                else:
                    print("You went into the mountains and died of frosbite.  You lose!")

            else:
                print("You lose!")

          elif ans == "across":
            print("You went across but you were bitten by a swamp snake and lost 4 hearts")
            hearts -= 4
            if hearts > 0:
                print(f"You made it to the other side of the swamp alive. You have {hearts} hearts")
                #mountians v froest
                ans = input("You conintue along the path and find a fork in the road. You can go thru the forest or into the mountains. Where do you go?(forest/mountains) ").lower()
                if ans == "forest":
                    print("You decided to go thru the forest and ate some poisonous berries and lost 5 hearts")
                    hearts -= 5
                    if hearts > 0:
                        print("You made it home alive")
                    else: 
                        print("You died in the forest. You lose!")
                else:
                    print("You went into the mountains and died of frosbite.  You lose!")
          else:
            print("not a valid answer! start over")

        else:
          print("You fell down a hole and died immediately....")

    else:
      print("Goodbye")
    
elif age >= 13:
    print('You can play with parent supervision!')
else:
    print("You are not old enough to play...")
