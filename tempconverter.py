import time
temp = float(input("Enter your temperature: "))
unit = input("Enter your unit (C/F): ").upper()
if unit == "C":
    print(f"The temperature is {temp} degrees Celcius.")
elif unit == "F":
        print(f"The temperature is {temp} degrees Farenheit.")
else:
    print(f"{unit} is not a valid unit.")
# Converter to convert your degrees to Celcius or vice versa
convert = input("Would you like to convert your unit to Celcius/Farenheit? (Y/N): ").upper()
if convert == "Y":
    if unit == "C":
        resultC = float(temp) * 9 / 5 + 32
        print(f"Your temperature in Farenheit is {resultC:.1f} degrees.")
    elif unit == "F":
        resultF = (float(temp) - 32) * 5 / 9
        print(f"Your temperature in Celcius is {resultF:.1f} degrees.")
else:
    if convert == "N":
        print("Thank you for giving us your temperature information!")
time.sleep(3)

