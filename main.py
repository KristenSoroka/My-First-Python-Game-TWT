print("Welcom To My First Python Game!")
#Youtube Tech with Tim https://youtu.be/7R-CfL21zIY
#Choose your own adventure style game

#greeting
name = input('What is your name? ')
age = int(input('What is your age? '))
print(f'Hello, {name.upper()}! Welcome to your own adventure game! You are {age} years old.')

#age verification
if age >=18:
    print("You are old enough to play!")
    
    wants_to_play = input('Do you want to play? ')
    if wants_to_play == "yes":
        print("Lets Play!")
    
elif age >= 13:
    print('You can play with parent supervision!')
else:
    print("You are not old enough to play...")
