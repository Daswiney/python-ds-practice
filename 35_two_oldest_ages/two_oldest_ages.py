def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """
    # Sort the ages in descending order
    sorted_ages = sorted(ages, reverse=True)

    # Initialize variables to store the two oldest ages
    oldest = None
    second_oldest = None

    for age in sorted_ages:
        # If we find the first distinct oldest age, store it as oldest
        if oldest is None:
            oldest = age
        # If we find the second distinct oldest age, store it as second_oldest
        elif age != oldest and second_oldest is None:
            second_oldest = age
        # If we have found both oldest and second_oldest, break the loop
        elif age != oldest and age != second_oldest:
            break

    return (second_oldest, oldest)

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.