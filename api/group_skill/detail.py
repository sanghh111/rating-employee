from http.client import OK
from sys import exec_prefix
from rest_framework.viewsets import ViewSet
from core.models import GroupSkill, Skill
from .serializers import GroupSkillRequestSerializer, GroupSkillSerializer, SkillSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import orjson
from django.db.models import F
from api.base.api_view import CustomAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
class GroupSkillDetailViewSet(CustomAPIView):

    queryset = GroupSkill.objects.all()
    @swagger_auto_schema(
        operation_description="UPDATE GROUP SKILL",
        request_body= openapi.Schema(
            type= openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(description="ID group skill",type = openapi.TYPE_INTEGER),
                'group_skill_name': openapi.Schema(description="Name group skill",type = openapi.TYPE_INTEGER),
            },
        ),
        responses= {
            200 : 'update success',
            400 : 'data invalid',
            404 : 'not found group skill',
            500 : 'Expection'
        })
    def update(self, request):
        # permission

        serializer = GroupSkillRequestSerializer(data= request.data)

        if serializer.is_valid(raise_exception= True):
            data =serializer.data
        else:
            return Response("Data invalid",400)
        
        try:
            group_skill = GroupSkill.objects.get(pk=id)
            group_skill.group_skill_name = data['group_skill_name']
            try:
                group_skill.save()
                return("update sucess",200)
            except Exception as e:
                return (e,500)
        except :
            return Response("NOT FOUND",404)

    @swagger_auto_schema(
        operation_description="Delete Group skill by id",
        request_body = openapi.Schema(
            type= openapi.TYPE_OBJECT,
            properties= {
                'id': openapi.Schema(description="id group skill",type=openapi.TYPE_INTEGER),
            },
        ),
        responses= {
            200 : 'OK',
            400 : 'DATA INVALID',
            404 : 'NOT FOUND',
            500 : 'EXPECTION'
        } 
    )
    def delete(self, request):
        # permission

        serializer = GroupSkillRequestSerializer(data = request.data)
        if serializer.is_valid(raise_exception= True):
            data =serializer.data 
        else:
            return Response(
                data = "Data invalid",
                status= 400
            )
        try:
            group_skill = GroupSkill.objects.get(pk=data['id'])
            try:
                group_skill.delete()
            except Exception as e:
                return (e,500)
        except GroupSkill.DoesNotExist:
            return Response("Not found",404)


class SkillDetailViewSet(CustomAPIView):

    queryset = Skill.objects.all()

    @swagger_auto_schema(
        operation_description="SKILL DETAIL",
        responses= {
            200 : "OK",
            404 : "NOT FOUND"
        }
    )
    def get_detail(self, request,*args, **kwargs):
        # permission

        try:
            skill = Skill.objects.filter(**kwargs).annotate(
                skill_id=F('id'),
                skill_name=F('name'),
                group_skill_name=F('group_skill_id__group_skill_name'),
            ).values(
                'skill_id',
                'skill_name',
                'group_skill_name',
            ).first()
            return Response(skill)
        except Skill.DoesNotExist:
            return Response("NOT FOUND",404)

    @swagger_auto_schema(
        operation_description="UPDATE SKILL",
        request_body= openapi.Schema(
            type= openapi.TYPE_OBJECT,
            properties= {
                'name':openapi.Schema(description='name skill',type= openapi.TYPE_STRING)
            }
        ),
        responses={
            200 : "OK",
            400 : "DATA INVALID",
            404 : "NOT FOUND",
            500 : "EXPECTION"
        }
    )
    def update(self, request,*args, **kwargs):
        # permission

        try:
            name = request.data['name']
        except KeyError:
            return ("DATA INVALID",400)
        try:
            skill = Skill.objects.get(**kwargs)
            skill.name = name
            try:
                skill.save()
                return Response("OK",200)
            except Exception as e:
                return Response(e,500)
        except Skill.DoesNotExist:
            return Response("NOT FOUND",404)


    @swagger_auto_schema(
        operation_description="Delete skill",
        responses={
            200 : "OK",
            404 : "NOT FOUND"
        }
        )
    def delete(self, request,*args, **kwargs):
        # permission

        try:
            skill = Skill.objects.get(**kwargs)
            try:
                skill.delete()
                return Response("Deleted", status=status.HTTP_200_OK)
            except Exception as e:
                return Response(e,500)
        except Skill.DoesNotExist:
            return Response("Skill not found", status=status.HTTP_404_NOT_FOUND)