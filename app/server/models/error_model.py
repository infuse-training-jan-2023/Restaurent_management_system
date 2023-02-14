
class ErrorResponseModel(object):

    def __init__(self, data, error, message):
        self.data = data
        self.error = error
        self.message = message

    def __repr__(self) -> str:
        return {
            "data": self.data,
            "error": self.error,
            "message": self.message
        }

