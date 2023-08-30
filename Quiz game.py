"""This is a quizz game where player can answer the questions and the score will be determined by the number of questions the player has answered correctly"""
#This is the welcome statement
print("Hello!! Welcome to my quiz game!!")
#Asking the player if they want to play the game
answer = input("Do you want to play the game? ")
if answer.lower() != "yes":
    quit()
else:
   #if yes then asking player to enter their name 
   participant_name = input("Enter your name: ")
   print("Welcome " +participant_name,"!!")
score = 0
#Question 1
question_reply = input("What does CN stand for? ")
if question_reply.lower()=="computer networks":
    print("Correct!!")
    score += 1
else:
    print("Oops incorrect answer!")
    

#Question 2
question_reply = input("What does RAM stand for? ")
if question_reply.lower()=="random access memory":
    print("Correct!!")
    score += 1
else:
    print("Oops incorrect answer!")
    

#Question 3
question_reply = input("What does CDN stand for? ")
if question_reply.lower()=="content delivery network":
    print("Correct!!")
    score += 1
else:
    print("Oops incorrect answer!")
     

#Question 4
question_reply = input("What does HCI stand for? ")
if question_reply.lower()=="human computer interaction":
    print("Correct!!")
    score += 1
else:
    print("Oops incorrect answer!")
    

#Question 5
question_reply = input("What does DNS stand for? ")
if question_reply.lower()=="domain name system":
    print("Correct!!")
    score += 1
else:
    print("Oops incorrect answer!")
    

# Displaying the final score out of 5
print("You got "+str(score),"out of 5")