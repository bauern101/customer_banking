"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
# The Account class from the Accounts.py file is imported. -----------------------------------> (4 points)

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """

    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    #                     ↓↓↓ ------> Balance value holder // Balance exists now, so I can put it in.
    s_account = Account(balance, 0)
    #                           ↑↑↑ ---------> Incurred interest, starting at 0 here and over-written later because it does NOT exist yet
    
    #In the create_savings_account function, an instance of the Account class is created
    #   and the balance and interest parameters are passed to the Account class. ------------------------------> (6 points)    


  
    # Calculate interest earned
     #interest = balance * (apr/100 * months/12)
    interest = balance * (interest_rate/100 * months/12)  # This is the eq given, but it is not correct.
    # interest = balance * (1+(interest_rate/100))**(months/12) # APR interest is compounding.
    # The interest earned is calculated and assigned to a variable. --------------------------------------------> (4 points)

    # Update the savings account balance by adding the interest earned
    updated_balance = interest + s_account.balance
    # The savings account balance is updated by adding the interest earned 
    #          to the balance and assigned to a variable. -------------------------------------------------------> (4 points)


    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    s_account.set_balance(updated_balance)
    #The updated balance is passed to the set balance method using the instance of the Account class. -------------> (6 points)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    s_account.set_interest(interest)
    # The interest earned is passed to the set balance method using the instance of the Account class. -------------> (6 points)

    # Return the updated balance and interest earned. 
    return s_account.balance, s_account.interest
    # The updated balance and interest earned are returned by the function. ---------------------------------------->  (5 points)


# balance = 10000
# interest_rate= 7.5
# months = 20
# test = create_savings_account(balance, interest_rate, months)
# print(test)