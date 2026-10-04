city = "Lisbon"
temperature = 21.5
humidity = 68
is_raining = False

print(f"Weather report for {city}")
print(f"Temperature: {temperature} C")
print(f"Humidity: {humidity}%")
print(f"Raining: {is_raining}")

# The afternoon update changes two values
temperature = 24.0
is_raining = True

print("Afternoon update:")
print(f"Temperature: {temperature} C")
print(f"Raining: {is_raining}")

print(type(city), type(temperature), type(humidity), type(is_raining))
