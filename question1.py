def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"The temperature in Celsius is: {celsius:.2f}°C")
    except Exception as e:
        print(f"An error occurred during temperature conversion: {e}")
    finally:
        print("Thank you for using the weather forecast application!")

def main():
    while True:
        temperature_str = input("Please enter the temperature in Fahrenheit (or 'quit' to exit): ")
        if temperature_str.lower() == 'quit':
            break
        try:
            temperature_fahrenheit = float(temperature_str)
            fahrenheit_to_celsius(temperature_fahrenheit)
        except ValueError:
            print("Error: Please enter a valid numerical temperature.")

if __name__ == "__main__":
    main()
