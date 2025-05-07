def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if applicable.
    
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage (0-100)
    
    Returns:
    float: Final price after discount (if applicable)
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

def main():
    try:
        # Get user input
        original_price = float(input("Enter the original price of the item: "))
        discount = float(input("Enter the discount percentage (0-100): "))
        
        # Calculate final price
        final_price = calculate_discount(original_price, discount)
        
        # Display results
        if discount >= 20:
            print(f"Final price after {discount}% discount: ${final_price:.2f}")
        else:
            print(f"No discount applied. Original price: ${original_price:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()