class APIError(Exception):
    """
    Exception Handling for API Rate Limit Ecxceeded.
    
    Input:
    message: The eerror message passed to the exception.
    """
    def __init__(self, status, message):
        self.custom_message = f"Status: {status}. Message: {message}"
        super().__init__()