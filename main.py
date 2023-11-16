import pandas as pd
import pulp
from datetime import datetime, timedelta

# Define paths to the input data files (assuming they are in the same directory)
aircraft_path = "C:/Users/mrkha/OneDrive/Desktop/OPTYM/Aircraft.csv"
demands_path = 'C:/Users/mrkha/OneDrive/Desktop/OPTYM/Demands.csv'
airports_path = 'C:/Users/mrkha/OneDrive/Desktop/OPTYM/Airports.csv'
distance_time_path = 'C:/Users/mrkha/OneDrive/Desktop/OPTYM/Distance and Flying Time.csv'


# Read the data files with specified encoding
# Read the data files with 'latin-1' encoding
aircraft_data = pd.read_csv(aircraft_path, encoding='latin-1')
demands_data = pd.read_csv(demands_path, encoding='latin-1')
airports_data = pd.read_csv(airports_path, encoding='latin-1')
distance_time_data = pd.read_csv(distance_time_path, encoding='latin-1')



# Preprocess the data if needed (simplified for this example)
# For instance, convert datetime strings to datetime objects
demands_data['ScheduledDepDatetime'] = pd.to_datetime(demands_data['ScheduledDepDatetime'])
demands_data['ScheduledArrDatetime'] = pd.to_datetime(demands_data['ScheduledArrDatetime'])

# Define a MILP model using PuLP
model = pulp.LpProblem("Aircraft_Route_Optimization", pulp.LpMaximize)

# Decision variables
# For simplicity, only considering whether a flight leg is flown by a certain aircraft
flight_legs = demands_data['DemandID']
aircrafts = aircraft_data['AircraftID']
x = pulp.LpVariable.dicts("route",
                          ((i, j) for i in flight_legs for j in aircrafts),
                          cat='Binary')

# Objective function
# Assuming a simple objective function for demonstration: maximizing the number of flight legs flown
model += pulp.lpSum([x[(i, j)] for i in flight_legs for j in aircrafts])

# Constraints
# Each flight leg should be flown by exactly one aircraft
for i in flight_legs:
    model += pulp.lpSum([x[(i, j)] for j in aircrafts]) == 1, f"One_Aircraft_Per_Leg_{i}"

# Aircraft utilization constraint (simplified)
# Assuming each aircraft can only fly a certain number of legs (e.g., 3 for this example)
for j in aircrafts:
    model += pulp.lpSum([x[(i, j)] for i in flight_legs]) <= 3, f"Max_Legs_Per_Aircraft_{j}"

# Solve the model
model.solve()

# Extract the solution
solution = []
for i in flight_legs:
    for j in aircrafts:
        if pulp.value(x[(i, j)]) == 1:
            leg_data = demands_data[demands_data['DemandID'] == i]
            solution.append({
                "ScenarioID": "BaseScenario",  # Assuming a single base scenario for simplicity
                "AircraftID": j,
                "FlightLegSeqNumber": i,
                "DepAirport": leg_data['DepAirport'].values[0],
                "DepTime": leg_data['ScheduledDepDatetime'].values[0]
            })

# Convert the solution to a DataFrame
solution_df = pd.DataFrame(solution)

solution_df.head()
