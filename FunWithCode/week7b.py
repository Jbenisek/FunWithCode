# Use the file name mbox-short.txt as the file name
total = 0
avg = 0
count = 0
while True:
    filename = raw_input("Enter file name (mbox-short.txt), type 'done' when finished: ")
    if filename == 'done': break
    try:
        fileopen = open(filename)
        #print 'File openned'
    except:
        print 'Can\'t open file'

    for line in fileopen:
        if not line.startswith("X-DSPAM-Confidence:") : continue
        startloc = line.find(':')
        line = line[startloc+1:]
        line = line.strip()
        linefloat = float(line)
        count = count + 1
        total = total + linefloat
    avg = total / count
    print 'Average spam confidence:',avg
#print "Done"
