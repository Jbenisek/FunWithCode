# Use words.txt as the file name in the python27 or root folder
count = 0
def fileprint(fileopen, count):
    for line in fileopen:
        line = line.rstrip()
        line = line.upper()
        count = count + 1
        print line
    print count

while True:
    filename = raw_input("Enter file name: ")
    if filename == 'done':
        break
    else:
        try:
            fileopen = open(filename)
        except:
            print 'File not found'
    try:
        fileprint(fileopen, count)
    except:
        print 'Filed def'

print 'Done'
