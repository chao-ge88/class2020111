from car import Car

my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(28)
my_new_car.read_odometer()

my_old_car = Car('bmw','li740',2015)
print(my_old_car.get_descriptive_name())
my_old_car.update_odometer(23_500)
my_old_car.read_odometer()
my_old_car.increment_odometer(200)
my_old_car.read_odometer()