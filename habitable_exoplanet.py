from math import sqrt

def habitable_exoplanet(L, r):
    habitability = ''
    #if a planet is between the square root of L/1.1 or L/.54 astronomical units, it is habitable
    if r < sqrt(L/1.1):
        habitability = 'too hot'
    elif r > sqrt(L/.54):
        habitability = 'too cold'
    else:
        habitability = 'just right'

    return habitability

print(habitable_exoplanet(1.11, 1.04))