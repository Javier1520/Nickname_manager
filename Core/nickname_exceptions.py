class NoNickNamesAvailable(Exception):
    """Exception raised when no nicknames are available."""
    
    def __init__(self, message="No nicknames available."):
        self.message = message
        super().__init__(self.message)