import re


def is_email(email):
    """Check if an email is valid

    Args:
        email (str): Email address

    Returns:
        True if email is valid, False otherwise.

    """

    pattern = '[\.\w]{1,}[@]\w+[.]\w+'
    if re.match(pattern, email):
        return True
    else:
        return False
