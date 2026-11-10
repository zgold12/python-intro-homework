def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    print(f"{c}°C = {f:.1f}°F")
def fahrenheit_to_celsius(f):
    c = (f - 32) * 5/9
    print(f"{f}°F = {c:.1f}°C")

celsius_to_fahrenheit(-5)
fahrenheit_to_celsius(16)
fahrenheit_to_celsius(56)