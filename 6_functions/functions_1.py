""""
Greet the user
Ask the user for their name
ask user - using name- where they are travelling?
Ask the user what is the distance to < where they are travelling>?
Ask the user for their car economy (R/Km)
Ask the user for the price of fuel 
Return the cost of the trip - output to the terminal
"""


def greet_user():
    """This function greets the user, then collects the name of the user and asks the user (with their name) where they are travelling to?"""
    # greet the user
    print("Good day! ")
    # use the input function to collect the user name
    user_name = input("What is your name? \n")
    print(f"Good day {user_name}!, where are you travelling to? ")


def trip_info():
    """
    This function asks the user where they are travelling to and the distance. The function then converts the distance to an int.

    The function returns the destination (string) and the distance to destination (an integer).
    """
    # ask the user where they are travelling to
    destination = input(f"Enter destination.. \n")

    # ask the user for the distance to where they are travelling to
    distance_destination = input(
        f"What is the distance to {destination} in kilometers? \n"
    )  # str -> int

    # convert distance_destination to int
    distance_destination_int = int(distance_destination)
    # the function returns two values
    return destination, distance_destination_int

def trip_budget():
    """
    This function asks the user for their budget for this trip and converts this budget from a string type to an integer.
    The function returns the trip budget as an integer.
    """
    # ask the user for their budget
    budget = input("What is the budget for this trip? (R)\n")  # str -> int
    # convert budget to int
    budget_int = int(budget)
    # return the budget_int value
    return budget_int

def trip_cost(distance_destination_int):
    """
    This function calculates the cost of a trip based on the trip distance, car_economy, and fuel price.
    par:
    distance_destination_int (integer): The distance to the destination as an integer.


    returns
    cost_trip (float): The cost of the trip to this destination.
    """
    # ask the user for their car economy (L/km)
    car_economy = input("What is the fuel economy of your car? (L/km) \n")  # str - > float

    # convert car_economy to float
    car_economy_float = float(car_economy)

    # ask the user for the price of fuel
    fuel_price = input("What is the fuel price? \n")  # str -> float
    # convert fuel_price to float
    fuel_price_float = float(fuel_price)

    # calculate the cost_per_km (R/km)
    cost_per_km = car_economy_float * fuel_price_float

    # calculate the cost of the trip
    cost_trip = distance_destination_int * cost_per_km
    return cost_trip

def trip_decision(cost_trip, budget_int, destination):
    """
    This function gives a recommendation of whether the trip should be taken or not. This recommendation is based on the cost of trip and trip budget.

    par:
    cost_trip (float): the cost of the trip
    budget_int (int): the budget available for the trip.
    destination (str): the name of the destination 

    """
    # lets make a decision on whether to travel or not
    if cost_trip > budget_int:
        print(
            f"The cost of the trip to {destination} is R {cost_trip}. This is out of the budget - R{budget_int}"
        )
        print(f"I do not recommend a trip to {destination}")
    else:
        print(
            f"The cost of the trip to {destination} is R {cost_trip}. This is within the budget - R{budget_int}"
        )
        print(f"I recommend a trip to {destination}")


# greet the user
greet_user()

#  collect trip information
trip_destination, trip_distance = trip_info()

# get budget for trip
budget = trip_budget()

# calculate trip cost
cost_trip = trip_cost(trip_distance)

trip_decision(cost_trip,budget, trip_destination)
