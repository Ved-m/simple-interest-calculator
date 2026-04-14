"""
Simple Interest Calculator
A Python application to calculate simple interest.
"""

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    
    Args:
        principal (float): Principal amount
        rate (float): Annual interest rate (in percentage)
        time (float): Time period (in years)
    
    Returns:
        dict: Dictionary containing principal, rate, time, interest, and total amount
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative values")
    
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    
    return {
        "principal": principal,
        "rate": rate,
        "time": time,
        "interest": round(interest, 2),
        "total_amount": round(total_amount, 2)
    }

def main():
    """Main function to run the calculator."""
    print("=" * 50)
    print("Welcome to Simple Interest Calculator")
    print("=" * 50)
    
    try:
        # Get user inputs
        principal = float(input("\nEnter Principal Amount: $"))
        rate = float(input("Enter Annual Interest Rate (%): "))
        time = float(input("Enter Time Period (years): "))
        
        # Calculate interest
        result = calculate_simple_interest(principal, rate, time)
        
        # Display results
        print("\n" + "=" * 50)
        print("CALCULATION RESULTS")
        print("=" * 50)
        print(f"Principal Amount: ${result['principal']:.2f}")
        print(f"Annual Interest Rate: {result['rate']:.2f}%")
        print(f"Time Period: {result['time']:.2f} years")
        print(f"Simple Interest: ${result['interest']:.2f}")
        print(f"Total Amount: ${result['total_amount']:.2f}")
        print("=" * 50)
        
    except ValueError as e:
        print(f"\nError: {e}")
    except EOFError:
        print("\nProgram terminated.")

if __name__ == "__main__":
    main()
