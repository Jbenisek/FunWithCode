text = "X-DSPAM-Confidence:    0.8475";
startpos = text.find(':')
chopstart = text[startpos+1:]
print float(chopstart)





