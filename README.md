# Assignment-week-2-3
This is a repository to showcase my Assignment topic currency converter using API's to convert one form of currency to another according to current rate difference between each countries.


# Currency Converter (Python)

This is a simple Python program that converts currency using live exchange rates.

Instead of asking the user to enter currency codes, the program allows the user to select countries from a list, making it easier to use.

## Features
- Country-based currency selection
- Uses a free public exchange rate API
- Takes user input for amount
- Displays converted currency value in a clean format

## How It Works
1. User selects the source country
2. User selects the target country
3. User enters the amount
4. Program fetches live exchange rates from an API
5. Converted value is calculated and displayed

## Requirements
- Python 3
- requests library

Install dependency:
```bash
pip install requests
