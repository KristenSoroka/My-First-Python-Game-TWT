print("Welcom To My First Python Game!")
#Youtube Tech with Tim https://youtu.be/7R-CfL21zIY
#Choose your own adventure style game

#greeting
name = input('What is your name? ')
age = int(input('What is your age? '))
print(f'Hello, {name.upper()}! Welcome to your own adventure game! You are {age} years old.')
#health of player
health = 10

#age verification using if/elif/else and nested statements
if age >=18:
    print("You are old enough to play!")

    wants_to_play = input('Do you want to play?(yes/no) ').lower()
    if wants_to_play == "yes":
        print("Lets Play!")
        left_or_right = input("First choice....Left or Right?(left/right) ").lower()
        if left_or_right == "left":
          ans = input("Nice! You followed the path and reached a swamp.  Do you go across or go around?(across/around) ").lower()
          if ans == "around":
            print("You were attacked by swamp people and lost health")
          elif ans == "across":
            print("You were bitten by swamp snake and lost health")
          else:
            print("You Lose!")

        else:
          print("You fell down a hole and died...")

    else:
      print("Goodbye")
    
elif age >= 13:
    print('You can play with parent supervision!')
else:
    print("You are not old enough to play...")
