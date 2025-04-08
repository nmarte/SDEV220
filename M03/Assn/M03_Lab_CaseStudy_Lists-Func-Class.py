'''
Module 3 Lab - Case Study: Lists, Functions, and Classes
Author: Nelson Marte
Program Name and Version: vehicle_cataloger
completed 04-07-2025
Assignment:
Complete the following steps:
Write a Python app that has the following classes:
A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
year
make
model
doors (2 or 4)
roof (solid or sun roof).
Write an app that will accept user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
The app will then ask the user for the year, make, model, doors, and type of roof and store thdata in the attributes above.
The app will then output the data in an easy-to-read and understandable format, such as this:
  Vehicle type: car
  Year: 2022
  Make: Toyota
  Model: Corolla
  Number of doors: 4
  Type of roof: sun roof
'''
# Define super class
class Vehicle:
    def __init__(self, v_type):
        self.v_type = v_type
# Define subclass
class Automobile(Vehicle):
    def __init__(self, v_type, year, make, model, doors, roof):
        super().__init__(v_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def user_input():
    print("Please enter the following information about your vehicle:")
    
    # Car/sedan is default
    v_type = "sedan"
    
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    
    # Exception check input
    while True:
        doors = input("Number of doors (2 or 4): ")
        if doors in ['2', '4']:
            break
        print("Invalid input. Please enter either 2 or 4.")
    
    # Validate roof input
    while True:
        roof = input("Type of roof (solid or sun roof): ").lower()
        if roof in ['solid', 'sun roof']:
            break
        print("Invalid input. Please enter either 'solid' or 'sun roof'.")
    
    return v_type, year, make, model, doors, roof

def display_vehicle_info(vehicle):
    print("\nVehicle Information:")
    print(f"  Vehicle type:     {vehicle.v_type.title()}")
    print(f"  Year:             {vehicle.year}")
    print(f"  Make:             {vehicle.make.title()}")
    print(f"  Model:            {vehicle.model.title()}")
    print(f"  Number of doors:  {vehicle.doors}")
    print(f"  Type of roof:     {vehicle.roof.title()}")

def main():
    print("Welcome to the Vehicle Information App!")
    
    # Get user input
    v_type, year, make, model, doors, roof = user_input()
    
    # Create Automobile object
    sedan = Automobile(v_type, year, make, model, doors, roof)
    
    # Display the information
    display_vehicle_info(sedan)

if __name__ == "__main__":
    main()