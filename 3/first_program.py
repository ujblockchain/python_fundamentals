""""
Greet the user
Ask the user for their name
ask user - using name- where they are travelling?
Ask the user what is the distance to < where they are travelling>?
Ask the user for their car economy (R/Km)
Ask the user for the price of fuel 
Return the cost of the trip - output to the terminal
"""

# greet the user
print("Good day! ")
# use the input function to collect the user name
user_name = input("What is your name? \n")
# ask the user where they are travelling to
destination = input(f"Where are you travelling to {user_name}? \n")

# ask the user for the distance to where they are travelling to
distance_destination = input(
    f"What is the distance to {destination} in kilometres? \n"
)  # str -> int

# convert distance_destination to int
distance_destination_int = int(distance_destination)

# ask the user for their budget for the trip
budget = input("What is the budget for this trip? \n") # str -> int

# convert the budget to an integer
budget_int = int(budget)

# ask the user for their car economy (L/km)
car_economy = input("What is the fuel economy of your car? (L/km) \n")  # str - > float

# convert car_economy to float
car_economy_float = float(car_economy)

# ask the user for the price of fuel
fuel_price = input("What is the fuel price? \n")  # str -> float
# convert fuel_price to float
fuel_price_float = float(fuel_price)

# calculate cost_per_km
cost_per_km = car_economy_float * fuel_price_float


# calculate cost of trip
cost_trip = distance_destination_int * cost_per_km

if cost_trip > budget_int:

    print(f"The cost of the trip to {destination} is R{cost_trip}. This is out of the budget - R {budget_int} for this trip")
    print(f"I do not recommend a trip to {destination}")

else:
    print(f"The cost of the trip to {destination} is R{cost_trip}. This is within the budget - R{budget_int} for this trip")
    print(f"I recommend a trip to {destination}")
