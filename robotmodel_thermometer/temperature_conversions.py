from constants import Constants

def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

def convert_celsius_to_fahrenheit(celsius):
    return celsius * (9 / 5) + 32

def convert_power_to_temp(power, temp):
    joules = power * Constants.environment_interval
    deltaT = joules / Constants.water_volume / 4.186
    return temp + deltaT

def convert_deltaT_to_power(deltaT):
    joules = deltaT * Constants.water_volume * 4.186
    power = joules / Constants.environment_interval
    return power