def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    stack = []

    for char in parens:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if not stack:
                return False  # Closing parenthesis with no matching open parenthesis
            stack.pop()

    return len(stack) == 0  # True if stack is empty (balanced)