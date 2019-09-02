from rest_framework.response import Response
from rest_framework import status


# Custom Exception Classes
class MissingParameterInRequestException(Exception):
    """Raised when a required parameter is missing in request"""

    def __init__(self, param, example=None):
        message = "{} - is missing in request. Please provide valid value. {}".format(param, example or '')

        super(MissingParameterInRequestException, self).__init__(message)


class DoesNotExistInSystemException(Exception):
    """Raised when a required parameter is missing in request"""

    def __init__(self, db_table, value, example=None):
        message = "{0} - does not exist in table {1}. Please provide valid value. {}".format(
            value, db_table or '')

        super(DoesNotExistInSystemException, self).__init__(message)


# Custom Response Handlers
class BadRequestParamResponseHandler(object):
    """Decorator- catch MissingParamsException or others and return Bad Response"""

    def __init__(self, func_obj):
        self.func_obj = func_obj

    def __call__(self, *args, **kwargs):
        try:
            return self.func_obj(*args, **kwargs)
        except (MissingParameterInRequestException, DoesNotExistInSystemException) as exp:
            Response(data={'error': exp.message},
                     status=status.HTTP_400_BAD_REQUEST)
