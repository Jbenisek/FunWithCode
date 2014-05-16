# You must type done to exit this program!

largest = None
smallest = None
count = 0

def large():
    #First Pass
    if largest is None:
        largest = numfloated
        print "First Pass", largest, numfloated
        return largest
                
    #Second Pass
    elif numfloated > largest:
        largest = numfloated
        print "Second Pass", largest, numfloated
        return largest

    else:
        print 'Not large', largest, numfloated
        return largest

def small():
    #First Pass for None
    if smallest is None:
        smallest = numfloated
        print "First Pass", smallest, numfloated
        return smallest
                
    #Second Pass for smaller?
    elif numfloated < smallest:
        smallest = numfloated
        print "Second Pass", smallest, numfloated
        return smallest

    else:
        print 'Not large', smallest, numfloated
        return smallest
#Start Loop    
while True:
    #Get user input
    num = raw_input("Enter a number: ")
    #If user inputs done then break loop
    if num == "done" : break
    
    try:
        numfloated = float(num)

        try:
            #First Pass for None
            if largest is None:
                largest = numfloated
                print "First Pass", largest, numfloated
                                
            #Second Pass for larger?
            elif numfloated > largest:
                largest = numfloated
                print "Second Pass", largest, numfloated
            else:
            #Wasn't Larger
                print 'Not larger', largest, numfloated
                
                
        except:
            #Did largest fail?
            print 'largest failed'
            
        try:
            #First Pass for None
            if smallest is None:
                smallest = numfloated
                print "First Pass", smallest, numfloated
                                
            #Second Pass for smaller?
            elif numfloated < smallest:
                smallest = numfloated
                print "Second Pass", smallest, numfloated
                
            else:
            #Wasn't Smaller
                print 'Not smaller', smallest, numfloated
           
           
        except:
            #Did smallest fail?
            print 'smallest failed'
            
    except:
        #If Invalid input go back to start of loop
        print "Invalid input"
        continue
    
    #Count the number of loops and print
    count = count + 1
    print count
    

#After typing done print largest/smallest as int.       
print "Maximum is", int(largest)
print "Minimum is", int(smallest)