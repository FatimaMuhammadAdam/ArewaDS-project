#9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
#Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of 
#information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
#Make an instance called restaurant from your class. 
# Print the two attributes individually, and then call both methods.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Hasina Cetaring", "Nigerian")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
 #9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
#different instances from the class, and call describe_restaurant() for each instance.
# Create three different instances of the Restaurant class
restaurant1 = Restaurant("iya Ebeji", "Duste")
restaurant2 = Restaurant("Hasina", "niger")
restaurant3 = Restaurant("3 star", "nigeria")

# Call describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

#9-3. Users: Make a class called User. Create two attributes called first_name
#and last_name, and then create several other attributes that are typically stored 
#in a user profile. Make a method called describe_user() that prints a summary 
#of the user’s information. Make another method called greet_user() that prints 
#a personalized greeting to the user.
#Create several instances representing different users, and call both methods for each user.
class User:
    def __init__(self, first_name, last_name, age, location, school):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.school = school
    
    def describe_user(self):
        print(f"User profile: {self.first_name} {self.last_name} is {self.age} years old, located in {self.location}, and studing in {self.school}.")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")


# Create several instances representing different users
user1 = User("binta", "audu", 25, "KANO", "BUK")
user2 = User("zainab", "idI", 30, "ZARIA", "ABU")
user3 = User("INDO", "TALLE", 45, "DUTSE", "FUD")

# Call both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
#9-4. Number Served: Start with your program from Exercise 9-1 (page 162). 
#Add an attribute called number_served with a default value of 0. Create an 
#instance called restaurant from this class. Print the number of customers the 
#restaurant has served, and then change this value and print it again.
#Add a method called set_number_served() that lets you set the number 
#of customers that have been served. Call this method with a new number and 
#print the value again.
#Add a method called increment_number_served() that lets you increment 
#the number of customers who’ve been served. Call this method with any number 
# you like that could represent how many customers were served in, say, a day of business.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self. number_served =0
    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    def set_number_served(self, number):
        self.number_served = number
    def increment_number_served(self, number):
        self.number_served +=  number


restaurant = Restaurant("Hasina Cetaring", "Nigerian")
print(f'the resturant has served {restaurant.number_served} customers')
restaurant.number_served = 12
print(f"The restaurant has served {restaurant.number_served} customers.")
restaurant.number_served = 16
print(f"The restaurant has served {restaurant.number_served} customers.")
restaurant.number_served = 20
print(f"The restaurant has served {restaurant.number_served} customers.")

#9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
#  that increments the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the value of login_attempts
#to 0.Make an instance of the User class and call increment_login_attempts()
#several times. Print the value of login_attempts to make sure it was incremented 
#properly, and then call reset_login_attempts(). Print login_attempts again to 
#make sure it was reset to 0.
class User:
    def __init__(self, first_name, last_name, age, location, school):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.school = school
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User profile for {self.first_name} {self.last_name}:")
        print(f"school: {self.school}")
        print(f"Location: {self.location}")
        print(f"age: {self.age}")
    
    def greet_user(self):
        print(f"Welcome back, {self.first_name}!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        
# Creating an instance of the User class
user = User("binta", "audu", 25, "KANO", "BUK")

# Calling the increment_login_attempts() method several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Printing the value of login_attempts to make sure it was incremented properly
print(f"Number of login attempts: {user.login_attempts}")

# Calling the reset_login_attempts() method
user.reset_login_attempts()

# Printing the value of login_attempts to make sure it was reset to 0
print(f"Number of login attempts after reset: {user.login_attempts}")


#9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write 
#a class called IceCreamStand that inherits from the Restaurant class you wrote 
#in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of 
#the class will work; just pick the one you like better. Add an attribute called 
#flavors that stores a list of ice cream flavors. Write a method that displays 
#these flavors. Create an instance of IceCreamStand, and call this method.
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    def display_flavours(self):
        print("In our restuarant we sell icecream and the icecream has the following flavours")
        for flavor in self.flavors:
            print(f"\t- {flavor}")
my_icecream = IceCreamStand('banana flaour', 'vanilla flavour', ['chocolate'])
print(my_icecream.describe_restaurant())
print(my_icecream.display_flavours())

#9-7. Admin: An administrator is a special kind of user. Write a class called 
#Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) 
#or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list 
#of strings like "can add post", "can delete post", "can ban user", and so on. 
#Write a method called show_privileges() that lists the administrator’s set of 
#privileges. Create an instance of Admin, and call your method.
class User:
    def __init__(self, first_name, last_name, age, location, school):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.school = school
    
    def describe_user(self):
        print(f"User profile for {self.first_name} {self.last_name}:")
        print(f"school: {self.school}")
        print(f"Location: {self.location}")
        print(f"age: {self.age}")
    
    def greet_user(self):
        print(f"Welcome back, {self.first_name}!")
class Admin(User):
    def __init__(self, first_name, last_name, age, location, school):
        super().__init__(first_name, last_name, age, location, school)
        self.privileges = ["admin can add post", "admin can delete post", "admin can ban user"]
    
    def show_privileges(self):
        print("the privileges of the Administrator are:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin("Fatima", "Muhammad Adam", 25, "Dutse", "Federal Universisty Dutse")
admin.show_privileges()

# Write a separate Privileges class. The class should have one 
#attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
#Move the show_privileges() method to this class. Make a Privileges instance 
#as an attribute in the Admin class. Create a new instance of Admin and use your 
#method to show its privileges.
class Privileges:
    def __init__(self):
        self.privileges = ["admin can add post", "admin can delete post", "admin can ban user"]
        
    def show_privileges(self):
        print("The privileges that the admins has are as follows:")
        for privilege in self.privileges:
            print("- " + privilege)

class Admin:
    def __init__(self, name):
        self.name = name
        self.privileges = Privileges()
admin = Admin("Fatima Muhammad Adam")
admin.privileges.show_privileges()
#9-9. Battery Upgrade: Use the final version of electric_car.py from this section. 
#Add a method to the Battery class called upgrade_battery(). This method 
#should check the battery size and set the capacity to 100 if it isn’t already. 
#Make an electric car with a default battery size, call get_range() once, and 
#then call get_range() a second time after upgrading the battery. You should 
#see an increase in the car’s range.

class Car:
 """A simple attempt to represent a car."""
 def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
 
 def get_descriptive_name(self):
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()
 
 def read_odometer(self):
    print(f"This car has {self.odometer_reading} miles on it.")
 
 def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
        
        print("You can't roll back an odometer!")
 
 def increment_odometer(self, miles):
    self.odometer_reading += miles

 
class Battery:
 """A simple attempt to model a battery for an electric car."""
 
def __init__(self, battery_size=75):
 """Initialize the battery's attributes."""
 self.battery_size = battery_size
def describe_battery(self):
 """Print a statement describing the battery size."""
 print(f"This car has a {self.battery_size}-kWh battery.")
def get_range(self):
 """Print a statement about the range this battery provides."""
 if self.battery_size == 75:
    range = 260
 elif self.battery_size == 100:
    range = 315
 
 print(f"This car can go about {range} miles on a full charge.")
 
class ElectricCar(Car):
 def __init__(self, make, model, year):
     super().__init__(make, model, year)
     self.battery = Battery()
#here is the newly upgrade battery 
 def ugrade_battery(self):
  if self.battery_size < 100:
     self.battery_size = 100

my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.get_range() 
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
