from unitconvert import temperatureunits
tc = float(input('Digite a temperatura em °C: '))
tf1 = temperatureunits.TemperatureUnit(tc, 'C', 'F').doconvert()
tf2 = 9*tc/5+32
print(f'A temperatura de {tc}°C equivale a {tf1}°F.')
print(f'A temperatura de {tc}°C equivale a {tf2}°F.')
