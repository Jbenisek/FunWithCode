## python 2.7 by Jeremy Benisek
# How do you feel?

# Start with 0 and False
ageinted = 0
ageintstatus = False
# Input your name
name = raw_input("Enter your name please: ")
# Print a Welcome message with inputed name
print "Hello and Welcome",name
# While True, if false re-enter age with a number
while True:
    age = raw_input("Enter your age in years: ")
    try: 
        ageinted = float(age)
        ageintstatus = True
    except:
        print "Something didn't work right"
    if ageintstatus == True:
        howdoesitfeel = raw_input("How does it feel to be your age: ")
        print str(ageinted) + "?"
        print str(howdoesitfeel) + " is how it feels to be " + str(ageinted)
        break
    else:
        print "You didn't enter a number"
else:
    print "failed"