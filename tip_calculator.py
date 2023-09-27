# tip_calculator.py

# TODO: Create a function named calculate_tip
# try:  #DO NOT MODIFY

def tip_calculator():
    try:
    # TODO:
        # Get these user inputs
        # total_cost (float): The cost of the meal (without tax)
        # num_people (int): The number of people splitting the bill
        # tip_percentage (float): The tip percentage
    
        total_cost = float(input("What is the cost of the meal (without tax): "))
    
        num_people = int(input("How many people are splitting the bill?: "))
    
        tip_percentage = float(input("Enter the tip percentage:/ ")) / 100

    # TODO:
        # Calculate the total bill including tip and sales tax (10%).
        # Convert to float: The total bill (including tip and sales tax).
    
        total_tip = tip_percentage * total_cost
    
        sales_tax = 0.10 * total_cost
        total_bill = total_cost + total_tip + sales_tax
    
        total_bill = float(total_bill)
    
        # total_tip = (tip_percentage / 100) * total_cost
    
        # sales_tax = 0.10 * total_cost
    # NOTE: Calculate the tip and tax separately. 
     
    # TODO: 
        # Calculate how much each person should pay.
        # Convert to float: The amount each person should pay.   
        bill_per_person = total_bill / num_people
        bill_per_person = float(bill_per_person)

    # TODO:
        # Using an f-string, print two different statements 
        # Total bill: $0.00
        # Each person should pay: $0.00
        print(f"Total bill: ${total_bill:.2f}")
        print(f"Each person should pay: ${bill_per_person:.2f}")

    # NOTE: The amounts are displayed with 2 decimals only

    # TODO: modify this except to include a Built-in Exception
        # TODO: Print an statement telling the user their input is invalid 
    
    except ValueError: 
        print("Your input is invalid. Please enter a valid number.")

    
if __name__ == "__main__": # DO NOT MODIFY # Double _ = "Dund"
    tip_calculator() # DO NOT MODIFY
