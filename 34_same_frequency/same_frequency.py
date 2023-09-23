def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    # Convert numbers to strings
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Check if the lengths of the two strings are different
    if len(str_num1) != len(str_num2):
        return False

    # Create dictionaries to store the frequency of each digit
    freq1 = {}
    freq2 = {}

    # Count the frequency of digits in num1
    for digit in str_num1:
        freq1[digit] = freq1.get(digit, 0) + 1

    # Count the frequency of digits in num2
    for digit in str_num2:
        freq2[digit] = freq2.get(digit, 0) + 1

    # Compare the frequency dictionaries
    return freq1 == freq2