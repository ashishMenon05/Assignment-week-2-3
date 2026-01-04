# make HTTP API calls because nothing else works ahhhhhhh!!!
import requests

#list a bit of countires here.
countries = {
    "India": "INR",
    "United States": "USD",
    "United Kingdom": "GBP",
    "European Union": "EUR",
    "Japan": "JPY",
    "Australia": "AUD",
    "Canada": "CAD",
    "China": "CNY"
}
print("Currency Converter\n")

# Display available countries at start when it runs?
print("Available Countries:")
for index, country in enumerate(countries, start=1):
    print(f"{index}. {country}")

try:
    from_choice = int(input("\nConvert FROM (enter number): "))
    to_choice = int(input("Convert TO (enter number): "))
    amount = float(input("Enter amount: "))

# adding a value error cause sometimes idk what is happeneing to the code bruh
except ValueError:
    print("Invalid input. Please enter numbers only.")
    exit()

# Convert dict->index 
country_list = list(countries.keys())

if from_choice < 1 or to_choice < 1 or from_choice > len(country_list) or to_choice > len(country_list):
    print("Invalid country selection.")
    exit()

from_currency = countries[country_list[from_choice - 1]]
to_currency = countries[country_list[to_choice - 1]]

try:
    # Building api url using the source currency because nothing else is working and idk why?
    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    # Send request to the free exchange rate API
    response = requests.get(url)

    #json format conversion
    data = response.json()


    if data["result"] != "success":
        print("Could not fetch exchange rates.")
        exit()


    rate = data["rates"][to_currency]
    converted_amount = amount * rate
    rate = round(rate, 4)
    converted_amount = round(converted_amount, 2)

    # ..................................................Displaay result.................................................
    print("\nConversion Result")
    print("-----------------")
    print("From Currency :", from_currency)
    print("To Currency   :", to_currency)
    print("Exchange Rate :", rate)
    print("Converted Amt :", converted_amount)

except:
    # Handles network issues or API failures because other tricks were not working........
    print("Error fetching data from API.")
