class InputException(Exception):
    """Raised when something wrong with input publication"""

    def __init__(self, message: str):
        self.message = message
