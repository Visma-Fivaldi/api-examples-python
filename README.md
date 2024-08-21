# Fivaldi API Python examples

This repository contains Python examples demonstrating how to interact with our API, including how to authenticate and how to send requests.

## Requirements

- Python 3.6 or higher
- Access to the terminal or command prompt

## Setup

Ensure Python 3 is installed on your system. You can verify this by running `python --version` or `python3 --version` in your terminal.

## Running the Scripts

1. **Navigate to the Script Directory**: Open a terminal or command prompt and navigate to the directory containing the scripts. Example: If your scripts are in `Documents/scripts/api-examples-python`, use `cd Documents/scripts/api-examples-python`.

2. **Set Environment Variables**: Before running scripts, set environment variables for your `PARTNER_ID` and `PARTNER_SECRET`.
    - **Linux/macOS**: `export PARTNER_ID="your_partner_id"` and `export PARTNER_SECRET="your_partner_secret"`
    - **Windows**: `set PARTNER_ID="your_partner_id"` and `set PARTNER_SECRET="your_partner_secret"`

3. **Run the Script**: Execute the script by running `python get_example.py` or `python3 get_example.py`, depending on your Python installation. Ensure your machine has internet access as the scripts communicate with an online API endpoint.

## Note

Replace `"your_partner_id"` and `"your_partner_secret"` with the actual credentials provided.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.