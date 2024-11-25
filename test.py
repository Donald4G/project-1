class Car:
    def __init__(self, make, model, year):
        # Private attributes (with a leading underscore)
        self._make = make
        self._model = model
        self._year = year

    # Getter method to access the private attribute
    def get_info(self):
        return f"{self._year} {self._make} {self._model}"

    # Setter method to update the private attribute
    def set_year(self, year):
        if year > 1885:  # The first car was made in 1886
            self._year = year
        else:
            print("Invalid year")


# Creating an object of Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing the car's information using a method
print(my_car.get_info())  # Output: 2020 Toyota Corolla

# Trying to update the year using setter method
my_car.set_year(2025)
print(my_car.get_info())  # Output: 2025 Toyota Corolla

# Trying to set an invalid year
my_car.set_year(1800)  # Output: Invalid year
