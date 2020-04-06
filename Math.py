import numpy as np
import pandas as pd
import csv

#SIR model equations

#Force of infection
def force_of_infection(percent_pop_infected, transmission_rate=0.05):
  gamma = transmission_rate * percent_pop_infected
  return gamma

#dS/dt: (S is the number of people that are susceptible) = susceptible_rate

def susceptible_rate(a, S, I):
	return a * S * I * (-1)

#dI/dt (I is the number of people that are infected) = infected_rate

def infected_rate(a, b, S, I):
	return a * S * I - b * I

#dR/dt (R is the number of people that have recovered) = recovered_rate

def recovered_rate(b, I)
	return b * I
############################################
#Canada's population:
N = 37660320

data = csv.reader(open('Recovered.csv', 'r'), delimiter=",")
recovered_date, recovered_value = [], []

for row in data:
  if row[1] == "Canada":
    recovered_date.append(row[4])
    recovered_value.append(row[5])


data = csv.reader(open('Infected.csv', 'r'), delimiter=",")
infected_date, infected_value = [], []

for row in data:
  if row[1] == "Canada":
    infected_date.append(row[4])
    infected_value.append(row[5])