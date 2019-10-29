#Python Richter Scale Calculation
#Your first and last name: Yosef Davidowitz
#Your ID: s1284597

#Algorithm:
# ask the user to 'Enter the Richter scale value: '
#   hint1: use an 'input' statement to input a variable called 'richter'
#   hint2: make sure 'richter' is a 'floating point' by using 'float'
# determine the Effect for the Richter scale value entered
#   hint1: use 'if' 'elif' and 'else' statements
#   hint2: remember to use ':' following all 'if' 'elif' and 'else' statements
# display or print the Effect
#   hint: use 'print' statement (only 1 effect should print)

# test your program several times with the following values:
#   8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6

askAgain = True
while askAgain == True:
    richter = float(input("Enter the Richter scale value or -99 to end: "))
    
    if richter == -99:
        break
    elif richter < 0:
        print("Value must be greater than 0")
    else:
        askAgain = False


    if richter >= 8:
        print("Most structures fall")
    elif richter >= 7:
        print("Many buildings are destroyed")
    elif richter >= 6:
        print("Many buildings considerably damaged, some collapse") 
    elif richter >= 4.5:
        print("Damge to poorly constructed buildings")
    elif richter >= 0:
        print("No destruction of buildings")
