def compare_numbers(number, user_guess):
    """
    Compares the number and the user guess and returns cows and bulls.
    A bull is when the digit is correct and in the right place.
    A cow is when the digit is correct but in the wrong place.
    """
    cow = 0
    bull = 0
    
    # Convert to strings to handle each digit separately
    number = str(number).zfill(4)
    user_guess = str(user_guess).zfill(4)

    for i in range(4):
        if user_guess[i] == number[i]:
            bull += 1
        elif user_guess[i] in number:
            cow += 1

    return cow, bull
