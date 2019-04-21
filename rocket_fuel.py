from math import exp

v_e=2550
m=250000

def rocket_fuel(v):
    m_fuel = 0.0
    m_fuel = exp(v/v_e)-1
    m_fuel = m_fuel * m

    return m_fuel

print(rocket_fuel(11186.0))