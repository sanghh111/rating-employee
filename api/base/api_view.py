from typing import Generic
# from rest_framework.permissions import IsAuthenticated
# from api.base.authentication import TokenAuthentication
from .permissions import IsActiveUser
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ErrorDetail
from drf_orjson_renderer.renderers import \
    ORJSONRenderer as OriginalORJSONRenderer
import orjson

class CustomAPIView(GenericViewSet):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = [IsActiveUser]
    #serializer_class = EmptyRequestSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = None
        #self.sort = ORDER_BY_DESC  # default sort via children by desc
        self.order_by = 'id'

    def initial(self, request, *args, **kwargs):
        self.CLIENT_ENCODE = get_encode_header(request)
        if not self.CLIENT_ENCODE:
            self.renderer_classes = (ORJSONRenderer,)
        # super().initial(self, request, *args, **kwargs)
        self.check_permissions(request)

class BaseAPIView(CustomAPIView):
    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.user = request.user

def get_encode_header(request):
    if request:
        client_encode = request.META.get('HTTP_AUTHORIZATION',)
        try:
            client_encode = int(client_encode)
        except (TypeError, ValueError):
            client_encode = 1

        if client_encode == 0:
            return False
    return True

class ORJSONRenderer(OriginalORJSONRenderer):
    @staticmethod
    def default(obj):
        # resolve promises/lazy values if needed
        if isinstance(obj, ErrorDetail):
            return str(obj)

        return OriginalORJSONRenderer.default(obj)



