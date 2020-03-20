#SIR model equations

#dS/dt: (S is the number of people that are susceptible) = susceptible_rate

def susceptible_rate(a, S, I):
	return a * S * I * (-1)

#dI/dt (I is the number of people that are infected) = infected_rate

def infected_rate(a, b, S, I):
	return a * S * I - b * I

#dR/dt (R is the number of people that have recovered) = recovered_rate

def recovered_rate(b, I)
	return b * I
