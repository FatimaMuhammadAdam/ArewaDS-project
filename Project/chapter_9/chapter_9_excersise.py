#Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
#Make a method called describe_restaurant() that prints these two pieces of 
#information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
#Make an instance called restaurant from your class. 
# Print the two attributes individually, and then call both methods.
class Restaurant:
    def _init_(self, restaurant_name, cuisine_type):
        self.restuarant_name =restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restuarant():
        print(f"the resturant has the following information{'restaurant_name'} and {'cuisine_type'}")

    def open_restuarantant():
        print(f"{'restuarant_name'} is open")

my_restuarant = Restaurant('stone casttle', 'asian restuarant')
print(f"My restuarant name is {my_restuarant.restuarant_name}.")
print(f"My restuarant type {my_restuarant.cuisine_type}.")
