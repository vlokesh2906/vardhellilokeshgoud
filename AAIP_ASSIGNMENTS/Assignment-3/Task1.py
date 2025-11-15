def calculate_electricity_bill():
    print("\n=== Electricity Bill Calculator ===")
    
    # Get customer details
    customer_name = input("Enter Customer Name: ")
    customer_number = input("Enter Customer Number: ")
    billing_month = input("Enter Billing Month: ")
    
    try:
        # Get meter readings
        previous_reading = float(input("Enter Previous Units (PU): "))
        current_reading = float(input("Enter Current Units (CU): "))
        
        # Validate readings
        if current_reading < previous_reading:
            raise ValueError("Current reading cannot be less than previous reading!")
        
        # Calculate units consumed
        units_consumed = current_reading - previous_reading
        
        # Get customer type
        print("\nSelect Customer Type:")
        print("1. Domestic")
        print("2. Commercial")
        print("3. Industrial")
        customer_type = input("Enter type (1/2/3): ")
        
        # Set rates based on customer type and consumption
        if customer_type == "1":  # Domestic
            if units_consumed <= 100:
                energy_rate = 3.50
            elif units_consumed <= 200:
                energy_rate = 4.50
            else:
                energy_rate = 6.00
            fixed_charges = 50
            customer_charges = 25
        elif customer_type == "2":  # Commercial
            energy_rate = 8.00
            fixed_charges = 100
            customer_charges = 50
        elif customer_type == "3":  # Industrial
            energy_rate = 10.00
            fixed_charges = 150
            customer_charges = 75
        else:
            raise ValueError("Invalid customer type selected!")
            
        # Calculate all charges
        energy_charges = units_consumed * energy_rate
        electricity_duty = energy_charges * 0.09  # 9% ED charges
        total_amount = (energy_charges + fixed_charges + 
                       customer_charges + electricity_duty)
        
        # Print the detailed bill
        print("\n" + "=" * 50)
        print("ELECTRICITY BILL".center(50))
        print("=" * 50)
        print(f"Customer Name: {customer_name}")
        print(f"Customer Number: {customer_number}")
        print(f"Billing Month: {billing_month}")
        print("-" * 50)
        print(f"Previous Reading (PU): {previous_reading:.2f} units")
        print(f"Current Reading (CU): {current_reading:.2f} units")
        print(f"Units Consumed: {units_consumed:.2f}")
        print(f"Energy Rate: ₹{energy_rate:.2f}/unit")
        print("-" * 50)
        print("CHARGES BREAKDOWN:")
        print(f"EC (Energy Charges): ₹{energy_charges:.2f}")
        print(f"FC (Fixed Charges): ₹{fixed_charges:.2f}")
        print(f"CC (Customer Charges): ₹{customer_charges:.2f}")
        print(f"ED (Electricity Duty @9%): ₹{electricity_duty:.2f}")
        print("-" * 50)
        print(f"Total Bill Amount: ₹{total_amount:.2f}")
        print("=" * 50)
        
    except ValueError as e:
        print(f"Error: {e}")
        print("Please enter valid numerical values")

if __name__ == "__main__":
    while True:
        calculate_electricity_bill()
        choice = input("\nCalculate another bill? (y/n): ")
        if choice.lower() != 'y':
            break
    print("Thank you for using Electricity Bill Calculator!")
