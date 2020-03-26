# Белов Игорь
def DEG_P_N(polynom):
	for i in range(len(polynom) - 1, -1, -1):
		if polynom[i]!=0:
			return i
	return 0

# Белов Игорь
def LED_P_Q(polynom):
	for i in range(len(polynom) - 1, -1, -1):
		if polynom[i]!=0:
			return polynom[i]
	return 0;
