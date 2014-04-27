hrs = raw_input("Enter Hours: ")
pay = raw_input("Enter Pay: ")
gross = float(hrs) * float(pay)
if gross == 96.25:
    print "Correct! The awnser is",gross
else:
    print "Incorrect! Redo."

print "Finished"