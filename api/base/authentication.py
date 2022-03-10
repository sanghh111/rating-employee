
import base64
import binascii
from datetime import datetime
from django.contrib.auth.hashers import check_password, make_password
from rest_framework import exceptions, HTTP_HEADER_ENCODING
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from app.models import User


class CustomTokenAuthentication(BaseAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        pass

    def authenticate_header(self, request):
        return self.keyword

    def get_bearer_token(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            raise exceptions.AuthenticationFailed('Token not found')

        if len(auth) == 1 or len(auth) > 2:
            raise exceptions.AuthenticationFailed('Invalid token header')
        
        receive_token = auth[1]

        return receive_token

class TokenAuthentication(CustomTokenAuthentication): 

    @staticmethod
    def parse_token(key):
        try:
            receive_token = base64.b64decode(key)
            receive_token = receive_token.decode()

            _info_list = receive_token.split(':')
            if len(_info_list) != 2:
                return None, None

            user_id = _info_list[0]
            token = _info_list[1]

            return user_id, token
        except ValueError:
            return None, None

    def authenticate(self, request):
        user_id, token = self.parse_token(self.get_bearer_token(request))
        return self.check_user_id_and_token(user_id, token, request)

    def check_user_id_and_token(self, user_id, token, request=None):
        if not user_id or not token:
            raise exceptions.AuthenticationFailed('Invalid Token')

        user = User.objects.filter(id=user_id).first()     

        if not user or token != user.token:
            raise exceptions.AuthenticationFailed("exception_data(error_code=INVALID_TOKEN)")

        setattr(request, 'user', user)

        return user, token


class BasicAuthentication(BaseAuthentication):
    """
        HTTP Basic authentication against username/password.
    """
    www_authenticate_realm = 'api'

    def authenticate_header(self, request):
        return 'Basic realm="%s"' % self.www_authenticate_realm

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'basic':
            raise exceptions.AuthenticationFailed("exception_data(error_code=BASIC_AUTH_NOT_FOUND)")

        if len(auth) == 1 or len(auth) > 2:
            raise exceptions.AuthenticationFailed("exception_data(error_code=BASIC_AUTH_NOT_VALID)")

        try:
            auth_parts = base64.b64decode(auth[1]).decode(HTTP_HEADER_ENCODING).partition(':')
            username, password = auth_parts[0], auth_parts[2]
        except (TypeError, UnicodeDecodeError, binascii.Error):
            raise exceptions.AuthenticationFailed("exception_data(error_code=BASIC_AUTH_NOT_VALID)")

        return self.check_username_password(username, password, request)

    @staticmethod
    def check_username_password(username, password, request=None):
        if not username or not password:
            raise exceptions.AuthenticationFailed("Invalid Login")

        user = User.objects.filter(username=username).first()

        if user is None:
            raise exceptions.AuthenticationFailed("INVALID_LOGIN")

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("INVALID_LOGIN")

       # if not user.active_flag:
        #     raise exceptions.AuthenticationFailed(exception_data(error_code=DISABLED_USER))

        # if not user.email_confirmed_flag:
        #     raise exceptions.AuthenticationFailed(exception_data(error_code=INACTIVE_USER))
 
        user.last_login = datetime.now()
        user.save()

        setattr(request, 'user', user)

        return user, None  # authentication successful