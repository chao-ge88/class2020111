from random import choice

from car import  Car

my_beetle = Car('volkaswagen','beetle',2019)
print(my_beetle.get_descriptive_name())

players = ['ding','cui','xia','li']
p = choice(players)
print(f"{p}'s car is "
      f""
      f""
      f"{my_beetle.get_descriptive_name()}")