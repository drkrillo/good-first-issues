import logging
import app.config

class APIError(Exception):
    """
    Exception Handling for API Rate Limit Ecxceeded.
    
    Input:
    status: Status code of the API call.
    message: The eerror message passed to the exception.
    """
    def __init__(self, status, message):
        self.status = status
        self.message = message
        self.custom_message = f"APIError {self.status}: {message}"
        
        logging.error(self.custom_message)
        
        super().__init__(self.message)
        
    def __str__(self):
        return self.custom_message