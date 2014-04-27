import sys
# Playing with code - Python by Jeremy Benisek 04-26-14 v0002
# Basic sign-in and Hours times Pay with Verify.
# Things to try: More than 5 username, passwords fails - non-numbers or $ included in hours or pay - More than 5 fails at entering hours or pay.
usernames = "Bob"
passwords = "1234"

# Start while true loop if fails exit program
while True:
    # Limit while true loop to 5 tries after five print message to screen and exit program
    for retry in range(5):
        # Enter username
        print "Of all the names you could use I'd suggest 'Bob'"
        yourusername = raw_input("Username? ")
        # Check username vs stored username(s)
        if yourusername == usernames:
            print "Of all the passwords you could use I'd suggest '1234'"
            # Enter password
            yourpassword = raw_input("Password? ")
            # Check password vs stored password(s)
            if yourpassword == passwords:
                print "Welcome!",yourusername
                # Start while true loop, if fails then break to parent loop after printing a message to screen
                while True:
                    # Try up to 5 times
                    for retry in range(5):
                        print "---->Estimated to be 35 hours.<----"
                        # Enter hours(hrs)
                        hrs = raw_input("Enter Hours: ")
                        print "---->Estimated to be 2.75.<----"
                        # Enter pay
                        pay = raw_input("Enter Pay: ")
                        # Try to float hours(hrs) and pay, if fails print Incorrect and restart local loop
                        try:
                            gross = float(hrs) * float(pay)
                            print "That comes to:",gross
                            if gross == 96.25:
                                print "---->Correct! The awnser is",gross,"<----"
                                # Breaking loops to start over
                                break
                            else:
                                print "---->Incorrect! Redo!<----"
                        except:
                            print "---->Hours or Pay isn't a number or has a $, please remove and retry!<----"
                    else:
                        print "---->Too many failed tries exiting now!<----"
                        break
                break
            else:
                print "---->Incorrect Password! Please Retry!<----"
    else:
        print "---->Too many tries exiting now!<----"
        sys.exit()
else:
    print "---->Failed Start over!<----"
