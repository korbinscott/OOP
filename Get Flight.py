import InsectClass as I

mosquito = I.Insect("mosquito", 2, 4)
housefly = I.Insect("housefly", 2, 4)

mosquito.calc_flight()
housefly.calc_flight()


print(f"the {mosquito.get_name()} can fly up to {mosquito.get_flight()}")
print(f"the {housefly.get_name()} can fly up to {housefly.get_flight()}")
