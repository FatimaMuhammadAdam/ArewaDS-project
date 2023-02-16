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
    def name(self, first_name, last_name, school, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.school = school
        self.age =age
        self.location = location
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
