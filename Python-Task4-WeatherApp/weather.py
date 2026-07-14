import requests

API_KEY = "cef270f38d130b81170e536e830991cb"

while True:
    print("=" * 45)
    print("        WEATHER APPLICATION")
    print("=" * 45)

    city = input("Enter city name: ").strip()

    if city == "":
        print("City name cannot be empty.\n")
        continue

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code != 200:
            print("\nError:", data.get("message", "Unable to fetch weather"))
        else:
            temp_c = data["main"]["temp"]
            temp_f = (temp_c * 9 / 5) + 32

            humidity = data["main"]["humidity"]
            weather = data["weather"][0]["description"].title()
            wind = data["wind"]["speed"]

            print("\n------ WEATHER REPORT ------")
            print(f"City         : {data['name']}")
            print(f"Temperature  : {temp_c:.1f} °C")
            print(f"Temperature  : {temp_f:.1f} °F")
            print(f"Humidity     : {humidity}%")
            print(f"Condition    : {weather}")
            print(f"Wind Speed   : {wind} m/s")
            print("-----------------------------")

    except requests.exceptions.Timeout:
        print("\nError: Request timed out.")

    except requests.exceptions.ConnectionError:
        print("\nError: No internet connection.")

    except Exception as e:
        print("\nUnexpected Error:", e)

    again = input("\nCheck another city? (yes/no): ").lower()

    if again != "yes":
        print("\nThank you for using the Weather App!")
        break