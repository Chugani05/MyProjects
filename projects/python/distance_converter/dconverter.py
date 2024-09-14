def convert(value, from_unit, to_unit):
    conversions = {
        'kilometers': {'kilometers': 1, 'miles': 1 / 1.609344, 'meters': 1000, 'feet': 3280.84, 'yards': 1093.61, 'inches': 39370.1, 'millimeters': 1_000_000, 'centimeters': 100_000},
        'miles': {'kilometers': 1.609344, 'miles': 1, 'meters': 1609.344, 'feet': 5280, 'yards': 1760, 'inches': 63_360, 'millimeters': 1_609_344, 'centimeters': 160_934.4},
        'meters': {'kilometers': 1 / 1000, 'miles': 1 / 1609.344, 'meters': 1, 'feet': 3.28084, 'yards': 1.09361, 'inches': 39.3701, 'millimeters': 1000, 'centimeters': 100},
        'feet': {'kilometers': 1 / 3280.84, 'miles': 1 / 5280, 'meters': 1 / 3.28084, 'feet': 1, 'yards': 1 / 3, 'inches': 12, 'millimeters': 304.8, 'centimeters': 30.48},
        'yards': {'kilometers': 1 / 1093.61, 'miles': 1 / 1760, 'meters': 1 / 1.09361, 'feet': 3, 'yards': 1, 'inches': 36, 'millimeters': 914.4, 'centimeters': 91.44},
        'inches': {'kilometers': 1 / 39370.1, 'miles': 1 / 63360, 'meters': 1 / 39.3701, 'feet': 1 / 12, 'yards': 1 / 36, 'inches': 1, 'millimeters': 25.4, 'centimeters': 2.54},
        'millimeters': {'kilometers': 1 / 1_000_000, 'miles': 1 / 1_609_344, 'meters': 1 / 1000, 'feet': 1 / 304.8, 'yards': 1 / 914.4, 'inches': 1 / 25.4, 'millimeters': 1, 'centimeters': 1 / 10},
        'centimeters': {'kilometers': 1 / 100_000, 'miles': 1 / 160_934.4, 'meters': 1 / 100, 'feet': 1 / 30.48, 'yards': 1 / 91.44, 'inches': 1 / 2.54, 'millimeters': 10, 'centimeters': 1}
    }
    
    return round(value * conversions[from_unit][to_unit], 2)

while True:
    print("Select the unit to convert from:")
    print("1. Kilometers")
    print("2. Miles")
    print("3. Meters")
    print("4. Feet")
    print("5. Yards")
    print("6. Inches")
    print("7. Millimeters")
    print("8. Centimeters")
    units = ['kilometers', 'miles', 'meters', 'feet', 'yards', 'inches', 'millimeters', 'centimeters']
    
    try:
        from_unit = int(input("Enter the number for the unit to convert from (1-8): "))
        if from_unit < 1 or from_unit > 8:
            raise ValueError("Invalid selection. Please choose a number between 1 and 8.")
        
        to_unit = int(input("Enter the number for the unit to convert to (1-8): "))
        if to_unit < 1 or to_unit > 8:
            raise ValueError("Invalid selection. Please choose a number between 1 and 8.")
        
        value = float(input(f"Enter the amount of {units[from_unit - 1]} to convert: "))
        
        result = convert(value, units[from_unit - 1], units[to_unit - 1])
        print(f"{value} {units[from_unit - 1]} is equal to {result} {units[to_unit - 1]}.")
    
    except ValueError as e:
        print(e)
    
    response = input("Do you want to perform another conversion? (yes/no): ")
    if response.lower() in ["no", "n"]:
        break
