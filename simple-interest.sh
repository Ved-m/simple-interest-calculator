#!/bin/bash

# Simple Interest Calculator

# Function to calculate simple interest
calculate_simple_interest() {
    principal=$1
    rate=$2
    time=$3

    # Using bc for floating-point arithmetic
    interest=$(echo "scale=2; ($principal * $rate * $time) / 100" | bc)
    
    echo "=========================================="
    echo "CALCULATION RESULTS"
    echo "=========================================="
    echo "Principal Amount: $principal"
    echo "Annual Interest Rate: $rate%"
    echo "Time Period: $time years"
    echo "Simple Interest Earned: $interest"
    echo "=========================================="
}

# Main script execution
echo "=========================================="
echo "Welcome to the Simple Interest Calculator"
echo "=========================================="

# Get user inputs
read -p "Enter Principal Amount: " principal
read -p "Enter Annual Interest Rate (%): " rate
read -p "Enter Time Period (years): " time

# Validate inputs
if ! [[ "$principal" =~ ^[0-9]+(\.[0-9]+)?$ ]] || \
   ! [[ "$rate" =~ ^[0-9]+(\.[0-9]+)?$ ]] || \
   ! [[ "$time" =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
    echo "Error: Please enter valid numbers for all inputs."
    exit 1
fi

# Calculate and display the result
calculate_simple_interest $principal $rate $time
