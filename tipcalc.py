import time
total = float(input("Enter the amount you paid for food: "))
tip = float(input("Enter the percentage you would like to tip: "))
tipcalc = total * (tip / 100)
print(f"Your total tip is ${tipcalc:02}")
print(f"Your total amount paid is ${tipcalc + total:02}")
time.sleep(3)