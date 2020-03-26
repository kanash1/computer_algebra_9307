# Белов Игорь
def DEG_P_N(polynom):
    if len(polynom)==0:
		return 0
	for i in range(len(polynom) - 1, -1, -1):
		if polynom[i]!=0:
			return i
	return 0

# Белов Игорь
def LED_P_Q(polynom):
	if len(polynom)==0:
		return 0; #zero polynom
	else:
		for i in range(len(polynom) - 1, -1, -1):
			if polynom[i]!=0:
				return polynom[i]
	return 0; #also zero polynom
