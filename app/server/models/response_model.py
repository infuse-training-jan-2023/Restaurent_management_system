
class ResponseModel(object):

    def __init__(self, data, response, message):
        self.data = data
        self.response = response
        self.message = message

    def __repr__(self) -> str:
        return {
            "data": self.data,
            "response": self.response,
            "message": self.message
        }
