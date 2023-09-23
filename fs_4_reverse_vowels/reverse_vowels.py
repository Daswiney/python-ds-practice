def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiouAEIOU'
    s_list = list(s)
    vowel_positions = []

    # Find the positions and values of vowels in the string
    for i, char in enumerate(s):
        if char in vowels:
            vowel_positions.append((i, char))

    # Reverse the vowels
    vowel_positions.reverse()

    # Replace the vowels in the original string
    for position, vowel in vowel_positions:
        s_list[position] = vowel

    return ''.join(s_list)