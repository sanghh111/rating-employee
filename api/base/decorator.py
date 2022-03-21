from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def permission(codename):
    def has_permission(a_func):
        @wraps(a_func)
        def wrapTheFunction(self):
            #permission
            user = self.user
            if user.verify_permission(codename) == False:
                return Response("User not permission", status=status.HTTP_400_BAD_REQUEST)
        return wrapTheFunction
    return has_permission

def has_permission(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        #permission
        # user = self.user
        # if user.verify_permission('view_project') == False:
        #     return Response("User not permission", status=status.HTTP_400_BAD_REQUEST)
        print(123)
        a_func()
    return wrapTheFunction