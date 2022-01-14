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
hearts = 5


#age verification using if/elif/else and nested statements
if age >=18:
    print("You are old enough to play!")

    wants_to_play = input('Do you want to play?(yes/no) ').lower()
    
    if wants_to_play == "yes":
        print("Lets Play!")

        print(f"You are starting with {hearts} hearts")
        left_or_right = input("First choice....Left or Right?(left/right) ").lower()
        # Left or Right Choice
        if left_or_right == "left":
          ans = input("Nice! You followed the path and reached a swamp.  Do you go across or go around?(across/around) ").lower()
          # Across or around the swamp choice
          if ans == "around":
            print("You were attacked by swamp people and lost 3 hearts")
            hearts -= 3
            if hearts > 0:
                print(f"You made it to the other side of the swamp alive. You have {hearts} hearts")
                ans = input("You come to a fork in the road.  You can go left through the woods or right into the mountains.(left/right) ").lower()
                if ans == "left":
                    ans = input("you are traveling thru the forest and find anouther fork.  You can take the road less traveled(right) or the cleared path (left).  Which do you take? ").lower()
                    if ans = "right":
                      print()
                  
                  else
                    hearts = 0
                    print(f"You went into the mountains and died of frostbite during your journey. All remainng hearts are lost Hearts = {hearts}")
            else:
                print(f"Hearts = {hearts}, you died")
          elif ans == "across":
            print("You went across but you were bitten by a swamp snake and lost 2 hearts")
            hearts -= 2
            if hearts > 0:
                print(f"You made it to the other side of the swamp alive. You have {hearts} hearts")
                print("You come to a fork in the road.  You can go left through the woods or right into the mountains. (left/right")
            else:
                print(f"Hearts = {hearts}, you die")
            
          else:
            print("You Lose!")

        else:
          print("You fell down a hole and died immediately....")

    else:
      print("Goodbye")
    
elif age >= 13:
    print('You can play with parent supervision!')
else:
    print("You are not old enough to play...")
