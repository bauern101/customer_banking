"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account
# The Account class from the Accounts.py file is imported. ------------------------------> (4 points)

# Define a function for the CD Account
def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    #                     ↓↓↓ ------> Balance value holder // Balance exists now, so I can put it in.
    cd_account = Account(balance, 0)
    #                            ↑↑↑ ------> Incurred interest, starting at 0 here and over-written later because it does NOT exist yet

    # In the create_cd_account function, an instance of the Account class is created 
    #    and the balance and interest parameters are passed to the Account class. --------------> (6 points)



    # Calculate interest earned
     #interest = balance * (apr/100 * months/12)
    interest = balance * (interest_rate/100 * months/12)  # This is the eq given, but it is not correct.
    # interest = balance * (1+(interest_rate/100))**(months/12) # APR interest is compounding.
    # The interest earned is calculated and assigned to a variable. ---------------------------> (4 points)

    # Update the CD account balance by adding the interest earned
    updated_balance = interest + cd_account.balance
    # The CD account balance is updated by adding the interest earned 
    #        to the balance and assigned to a variable. ----------------------------------------------> (4 points)


    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    cd_account.set_balance(updated_balance)
    # The updated balance is passed to the set balance method using the instance of the Account class. ------- > (6 points)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    cd_account.set_interest(interest)
    # The interest earned is passed to the set balance method using the instance of the Account class. ------->  (6 points)

    # Return the updated balance and interest earned.
    return  cd_account.balance, cd_account.interest
    #The updated balance and interest earned are returned by the function. ------------------------------------> (5 points)


# balance = 10000
# interest_rate= 7.5
# months = 20
# test = create_cd_account(balance, interest_rate, months)
# print(test)