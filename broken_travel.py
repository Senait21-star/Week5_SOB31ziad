# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!!")
