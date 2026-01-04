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
<img width="802" height="412" alt="Screenshot 2026-01-05 022814" src="https://github.com/user-attachments/assets/3f44b2f1-50ae-4bc2-aaca-39e1e336ad3c" />
<img width="822" height="233" alt="Screenshot 2026-01-05 022541" src="https://github.com/user-attachments/assets/96de0b2a-deea-4385-9864-2dbc4fd8b963" />


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
