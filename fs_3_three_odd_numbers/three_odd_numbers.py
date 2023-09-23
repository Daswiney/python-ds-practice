def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    if len(nums) < 3:
        return False  # Not enough numbers to form a group of three

    for i in range(len(nums) - 2):
        group_sum = nums[i] + nums[i + 1] + nums[i + 2]
        if group_sum % 2 != 0:
            return True  # Found a group with an odd sum

    return False  # No group with an odd sum found