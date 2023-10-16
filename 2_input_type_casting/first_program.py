"""
Greet the user
Ask the user for their name
ask user - using name - where they are travelling?
Ask the user what is the distance to <where they are travelling>?
Ask the user for their car economy (R/Km)
Ask the user for the price of fuel (R/L)
Return the cost of the trip - output to the terminal
"""

# greet the user
print("Good day!")

# use the input function to collect the user's name
user_name  = input("What is your name? \n")

# ask the user for where they are travelling to
destination = input(f"Where are you travelling to {user_name}? \n")

# ask the user for the distance to where they are travelling to
distance_destination = input(f"What is the distance to {destination}?") # str -> int

# convert distance destination from string to int
distance_destination_int = int(distance_destination)

# ask the user for their car economy (R/Km)
car_economy = input("What is the fuel economy of your car (R\Km)? \n") # str - > float

# convert car_economy from string to float
car_economy_float  = float(car_economy)

# ask the user for the price of fuel
fuel_price = input("What is the price of fuel? \n") # str-> float

# convert fuel price from string to float
fuel_price_float = float(fuel_price)

# calculate cost of trip
cost_trip = distance_destination_int * car_economy_float

print(f"The cost of the trip to {destination} is R{cost_trip}")