def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """
    # Initialize a variable to keep track of the sum of character positions
    total = 0

    # Iterate through the characters in the word
    for char in word:
        # Convert the character to lowercase and calculate its character position
        char_position = ord(char.lower()) - ord('a') + 1
        total += char_position  # Add the character position to the total

    # Check if the total is odd
    return total % 2 == 1


    # Hint: you may find the ord() function useful here