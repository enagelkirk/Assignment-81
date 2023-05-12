class Vehicle:

  def set_Make_Model(self, make, model):
    self.vehicle_make = make
    self.vehicle_model = model

  def displayOption(self):
    print(f"The vechicle is a {self.vehicle_make} {self.vehicle_model}")

class Car(Vehicle):

  def setDoors(self, doors):
    self.car_doors = doors

  def displayOption(self):
    print(f"\nThe make and model of the car is: {self.vehicle_make} {self.vehicle_model}")
    print(f"Your car has {self.car_doors} doors.")

class Truck(Vehicle):
  
  def setBedLength(self, bedlength):
    self.bed_length = bedlength
  
  def displayOption(self):
    print(f"\nThe make and model of the truck is: {self.vehicle_make} {self.vehicle_model}")
    print(f"Your truck has a bed length of {self.bed_length}ft.")

print("Welcome to the Virtual Garage.")
def get_menu_option(): 

  menu_options = ('c', 't', 'q')

  while True:
    print()
    print("--- Menu ---")
    print("\nc = you want to enter a car")
    print("t = you want to enter a truck")
    print("q = quit the program")

    print()
    menu_choice = input("Enter an option: ")

    if menu_choice.lower() in menu_options:
      return menu_choice
    else:
      print()
      print("This is not an option")

while True:

  menu_choice = get_menu_option()

  if menu_choice == "c":
    print("\n--- Car Details ---")

    input_car_make = input("\nPlease enter the make of your car: ")
    input_car_model = input("Please enter the model of your car: ")
    input_doors = input("Please enter the number of doors your car has: ")
    new_car = Car()
    new_car.set_Make_Model(input_car_make, input_car_model)
    new_car.setDoors(input_doors)
    new_car.displayOption()

  elif menu_choice == "t":
    print("\n--- Truck Details ---")

    input_truck_make = input("\nPlease enter the make of your truck: ")
    input_truck_model = input("Please enter the model of your truck: ")
    input_bed_length = input("Please enter the length of the bed of your truck in ft: ")
    new_truck = Truck()
    new_truck.set_Make_Model(input_truck_make, input_truck_model)
    new_truck.setBedLength(input_bed_length)
    new_truck.displayOption()

  elif menu_choice == "q":
    print("\nNo more cars will be added to your virtual garage. Have a great day!")
    break