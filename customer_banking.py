# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    print("Welcome to the AI Bootcame Savings & Loan Bank, where youcan truly 'Invest in your future'.")
    print("Please provide your account information below.")
    savings_balance = float(input("What is your present saving balance?   ")) 
    savings_interest = float(input("What interest rate would you like calculated?   "))
    savings_maturity = int(input("How many months would you like the analysis preformed for?   "))
    # The user is prompted to set the savings balance, interest rate, and months for the savings account. ----------------> (8 points)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("\nTask Complete.\n")
    # formatted_number = f"{number:,.2f}"  # Formats to two decimal places and includes commas for thousands
    print(f"Your updated Savings Account Balance is ${updated_savings_balance:,.2f}, "
        f"with ${interest_earned:,.2f} in earned interest.\n")
    #Code is written to print out the interest earned and updated savings account balance
    # with interest earned for the given months. 
    #The values are formatted to two decimal places and thousandths. ----------------------------------------------------> (6 points)



    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("What is your present CD balance?   ")) 
    cd_interest = float(input("What interest rate would you like you CD calculated with?   "))
    cd_maturity = int(input("How many months would you like the analysis preformed for?   "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("\nTask Complete.\n")
    # formatted_number = f"{number:,.2f}"  # Formats to two decimal places and includes commas for thousands
    print(f"Your updated CD Balance is ${updated_cd_balance:,.2f}, "
        f"with ${interest_earned:,.2f} in earned interest.\n")
    print("\nThank you for banking with AI Bootcame Savings & Loan Bank")
    print("We wish you many happy returns!\n\n")

if __name__ == "__main__":
    # Call the main function.

    main()