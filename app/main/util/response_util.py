# WORKING IN PROGRESS
class ResponseMessage:
    def __init__(self):
        pass

    @staticmethod
    def success(message="sucess", data={}, http_code=None):
        response_object = {
            'success': True,
            'message': message,
        }
        return response_object, 409
