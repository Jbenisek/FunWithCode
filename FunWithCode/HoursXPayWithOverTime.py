hours = raw_input("Enter Hours:")
hoursfloated = float(hours)
rate = raw_input("Enter Rate:")
ratefloated = float(rate)
if hours <= 40:
    normalpay = hoursfloated * ratefloated
    print normalpay
else:
    # Over time starts at 41
	normalpay = 40 * ratefloated
	overtime = ((hoursfloated - 40) * (ratefloated * 1.5))
	totalpay = overtime + normalpay
	print totalpay