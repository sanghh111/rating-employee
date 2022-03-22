from rest_framework import status
from rest_framework.exceptions import APIException


class CustomAPIException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, status_code=status.HTTP_200_OK, detail=None):
        self.status_code = status_code
        self.detail = detail
