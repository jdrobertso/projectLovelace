from math import exp

v_e_dict = {
    "1": 617.5,
    "2": 4.25,
    "3": 10.36,
    "4": 11.186,
    "5": 2.38,
    "6": 5.03,
    "7": 0.51,
    "8": 60.20,
    "9": 2.558,
    "10": 2.025,
    "11": 2.741,
    "12": 2.440,
    "13": 36.09,
    "14": 2.639,
    "15": 21.38,
    "16": 23.56,
    "17": 1.455,
    "18": 1.23
}

m=250000
v_e=2550

print("Welcome to the rocket science program!")
print("Please enter the number of the planet you want to launch from: ")
selection = input("1. The Sun\n2. Mercury\n3. Venus\n4. Earth\n5. Earth's Moon\n6. Mars\n7. Ceres\n8. Jupiter\n9. Io\n10. Europa\n11. Ganymede\n12. Callisto\n13. Saturn\n14. Titan\n15. Uranus\n16. Neptune\n17. Triton\n18. Pluto\nEnter selection here: ")

v = v_e_dict.get(selection)

def rocket_fuel(v):
    m_fuel = 0.0
    m_fuel = exp(v/v_e)-1
    m_fuel = m_fuel * m

    return m_fuel

print("Saturn V will need %s fuel to escape from option %s" % (rocket_fuel(v), selection))