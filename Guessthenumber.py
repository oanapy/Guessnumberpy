# Hi teacher or student :)!
# I had some issues in writing the new_game() function
# and I got stuck on it, so it is not working according 
# to proffesor's indications. I'm sorry for this.
# If you have some pieces of advice on how the code should look,
# please share in general comments section :).
# Thanks in advance!
#
#
import random
import simplegui
import math

# initialize global variables used in your code
secret_number = 0
count = 7
rand_range = 100
# helper function to start and restart the game
def new_game():
    print "Let's play again! Hit the desired range button!"
    range100()
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global secret_number
    global count
    global rand_range
    rand_range = 100
    count = 7
    secret_number = random.randrange(0, rand_range)
    print "\n","Choose a number between 0 and 100"
    print "You have", count, "guesses", "\n"
    

def range1000():
    # button that changes range to range [0,1000) and restarts    
    global secret_number
    global count
    global rand_range
    rand_range = 1000
    count = 10
    secret_number = random.randrange(0, rand_range)
    print "\n"," Choose a number between 0 and 1000"
    print "You have",count, "guesses", "\n"
    
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number

    if int(guess) == secret_number:
        print "You win!"
        new_game()
    elif int(guess) in range(int(guess), secret_number):
        print "Higher!"
    else:
        print "Lower!"
        
    global count
    count -= 1
    print "Number of guesses remained is", count, ".", "\n"
  
    if count == 0:
        print "Your number of guesses exceeded the number of possible guesses!"       
        new_game()

# create frame
frame = simplegui.create_frame('Secret Number Game', 200, 200)


# register event handlers for control elements

button100 = frame.add_button('Range 0 -100', range100, 150)
button1000 = frame.add_button('Range 0 - 1000', range1000, 150)
input = frame.add_input('Your guess', input_guess, 100)


# call new_game and start frame
range100()
frame.start()