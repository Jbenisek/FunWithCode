hours = 0.0
rate = 0.0
normalpay = 0.0
overtime = 0.0
totalpay = 0.0

def computepay(normalpay, totalpay):
    if hoursfloated <= 40:
        normalpay = hoursfloated * ratefloated
        return normalpay
    else:
        # Over time starts at 41
        normalpay = 40 * ratefloated
        overtime = ((hoursfloated - 40) * (ratefloated * 1.5))
        totalpay = overtime + normalpay
        return totalpay

def tryfloat(x):
    try:
        x = float(x)
        return (x)
    except:
        print "Failed to Float, please check entry and retry, Error= hours = float(hours)"
    

hours = raw_input("Enter Hours:")
hoursfloated = tryfloat(hours)
rate = raw_input("Enter Rate:")
ratefloated = tryfloat(rate)

print computepay(normalpay, totalpay)
