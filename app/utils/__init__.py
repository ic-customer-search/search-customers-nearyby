import traceback


def exception_to_str(e: Exception) -> str:
    """
    Given an exception object, return its string representation with the stack trace.
    :param e: Exception object
    """
    return str(e) + "\n" + "".join(traceback.format_tb(e.__traceback__))
