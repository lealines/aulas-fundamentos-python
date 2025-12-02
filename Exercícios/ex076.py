def celsius_to_fahrenheit(celsius:float):
    print(f"{celsius}ºC <=> {((celsius*1.8) + 32):.2f} F")

celsius_to_fahrenheit(float((input("Insira a temperatura em celsius: "))))