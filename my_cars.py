from car import Car
from electric_car import ElectricCar as EC

my_tesla = EC('Tesla','roadster',2019)
print(my_tesla.get_descriptive_name())

my_beetle = Car('volkaswagen','beetle',2019)
print(my_beetle.get_descriptive_name())
