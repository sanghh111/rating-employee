from app.models import UserRole
#from .serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
import orjson
from django.db.models import F
from api.base.api_view import BaseAPIView