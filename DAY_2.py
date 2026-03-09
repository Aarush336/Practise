def check_water(temperatures):
    if temperatures > 39:
        return("Needs water")
    else:
        return("Normal")

temperatures = [38, 42, 35, 40, 33, 41, 37]
for temp in temperatures:
        print(temp, check_water(temp))