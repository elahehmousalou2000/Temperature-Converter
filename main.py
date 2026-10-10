temperature = float(input("Enter temperature: "))
unit = input("Enter unit (C/F): ").strip().upper()

if unit == "C":
    result = temperature * 9 / 5 + 32
    print(f"{temperature}°C = {result:.2f}°F")
elif unit == "F":
    result = (temperature - 32) * 5 / 9
    print(f"{temperature}°F = {result:.2f}°C")
else:
    print("Invalid unit. Use C or F.")
