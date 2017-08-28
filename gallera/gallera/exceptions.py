class AuthenticationException(Exception):
    def __init__(
            self, message='AuthenticationException',
            response=None, errors=None,
    ):
        super().__init__(self, message)
        self.errors = errors
        self.response = response


class BadRequestFormatException(Exception):
    """Exception launched when the request body could not be parsed according
    to the content type"""
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
