import pandas as pd


class DataPreprocessor:
    def __init__(self, aircraft_path, demands_path, airports_path, distance_time_path):
        self.aircraft_path = aircraft_path
        self.demands_path = demands_path
        self.airports_path = airports_path
        self.distance_time_path = distance_time_path

        # Dictionaries to hold processed data
        self.aircraft_data = None
        self.demands_data = None
        self.airports_data = None
        self.distance_time_data = None

    def load_data(self):
        # Load data from the provided file paths
        self.aircraft_data = pd.read_csv("C:\Users\mrkha\OneDrive\Desktop\OPTYM\Aircraft.csv")
        self.demands_data = pd.read_csv(self.demands_path)
        self.airports_data = pd.read_csv(self.airports_path)
        self.distance_time_data = pd.read_csv(self.distance_time_path)

    def process_aircraft_data(self):
        # Process and transform aircraft data as needed
        # Example: self.aircraft_data['New Column'] = self.aircraft_data['Existing Column'].apply(some_function)
        pass

    def process_demands_data(self):
        # Process and transform demands data as needed
        pass

    def process_airports_data(self):
        # Process and transform airports data as needed
        pass

    def process_distance_time_data(self):
        # Process and transform distance and flying time data as needed
        pass

    def preprocess_all(self):
        self.load_data()
        self.process_aircraft_data()
        self.process_demands_data()
        self.process_airports_data()
        self.process_distance_time_data()
        # Any additional processing steps can be added here
