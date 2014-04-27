Score = raw_input("Enter Grade Score: ")
try:
    ScoreFloated = float(Score)
    if ScoreFloated >= 0.9:
        print "A"
    elif ScoreFloated >= 0.8:
        print "B"
    elif ScoreFloated >= 0.7:
        print "C"
    elif ScoreFloated >= 0.6:
        print "D"
    elif ScoreFloated < 0.6:
        print "F"
except:
    print "Bad input"
