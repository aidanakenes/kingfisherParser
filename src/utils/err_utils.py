class ApplicationError(Exception):
    def __init__(self):
        self.code = 'APIError',
        self.message = f'Failed to parse page for item'
