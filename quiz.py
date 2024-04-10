
print("---Welcome to my Quiz---")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print ("Let's play.")

counter = 0

answer1 = input("What is the capital of India? ")

if answer1.lower() == 'delhi':
    print("Correct! The capital of India is Delhi.")
    counter += 1
else:
    print("Incorrect! The capital of India is Delhi.")
    
answer2 = input("What is the capital of USA? ")
    
if answer2.lower() == 'washington dc':
    print("Correct! The capital of USA is Washington DC.")
    counter += 1
else:
    print("Incorrect! The capital of USA is  Washington DC.")
    
answer3 = input("What is the capital of Italy? ")
    
if answer3.lower() == 'rome':
    print("Correct! The capital of Italy is Rome.")
    counter += 1
else:
    print("Incorrect! The capital of Italy is Rome.")
    
print("Your score is {} out of 3".format(counter))


    

