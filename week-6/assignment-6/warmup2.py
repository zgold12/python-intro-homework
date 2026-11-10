def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f
def fahrenheit_to_celsius(f):
    c = (f - 32) * 5/9
    return c

a = -5
b = 16
c = 56
d = celsius_to_fahrenheit(a)
e = fahrenheit_to_celsius(b)
f = fahrenheit_to_celsius(c)
print(f"{a}°C = {d:.1f}°F")
print(f"{b}°F = {e:.1f}°C")
print(f"{c}°F = {f:.1f}°C")