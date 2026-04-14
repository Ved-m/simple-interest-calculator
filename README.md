# Simple Interest Calculator

A straightforward Python application to calculate simple interest based on principal amount, interest rate, and time period.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Formula](#formula)
- [Example](#example)
- [License](#license)

## Description

This project provides a simple interest calculator that takes three inputs:
- **Principal Amount**: The initial sum of money
- **Annual Interest Rate**: The percentage rate per annum
- **Time Period**: The duration in years

The calculator then computes the simple interest earned and the total amount (principal + interest).

## Features

- ✅ Easy-to-use command-line interface
- ✅ Input validation for negative values
- ✅ Precise calculations with rounded results
- ✅ Clear, formatted output display
- ✅ Error handling for invalid inputs

## Installation

### Prerequisites
- Python 3.6 or higher

### Steps
1. Clone the repository:
```bash
git clone https://github.com/Ved-m/simple-interest-calculator.git
```

2. Navigate to the project directory:
```bash
cd simple-interest-calculator
```

## Usage

Run the calculator with:
```bash
python simple_interest_calculator.py
```

Follow the prompts to enter:
1. Principal Amount (in currency)
2. Annual Interest Rate (in percentage)
3. Time Period (in years)

The calculator will display:
- The interest earned
- The total amount at the end of the period

## Formula

Simple Interest is calculated using the formula:

```
SI = (P × R × T) / 100
```

Where:
- **SI** = Simple Interest
- **P** = Principal Amount
- **R** = Annual Interest Rate (%)
- **T** = Time Period (years)

**Total Amount** = Principal + Simple Interest

## Example

```
Enter Principal Amount: $1000
Enter Annual Interest Rate (%): 5
Enter Time Period (years): 2

CALCULATION RESULTS
==========================================
Principal Amount: $1000.00
Annual Interest Rate: 5.00%
Time Period: 2.00 years
Simple Interest: $100.00
Total Amount: $1100.00
==========================================
```

In this example:
- Principal: $1000
- Interest Rate: 5%
- Time: 2 years
- **Simple Interest Earned**: $100
- **Total Amount**: $1100

## Code Structure

- `simple_interest_calculator.py` - Main Python file containing:
  - `calculate_simple_interest()` - Core calculation function
  - `main()` - User interface function

## License

This project is open source and available under the MIT License.

## Author

Created as a Coursera assignment project.

---

**Happy Calculating!** 🧮
