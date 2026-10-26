# 1. Načtení teploty a převod na float
celsius = float(input("Zadejte teplotu ve stupních Celsia: "))

# 2. a 3. Výpočet a zaokrouhlení na 2 desetinná místa
fahrenheit = round(celsius * 9 / 5 + 32, 2)
kelvin = round(celsius + 273.15, 2)

# 4. Výpis pomocí f-stringu
print(f"{celsius} °C = {fahrenheit} °F = {kelvin} K")
