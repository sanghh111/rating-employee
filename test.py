import os
from tokenize import Pointfloat

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rating_employee.settings')


django.setup()

from core.user.models import User,RolePermission
from core.project.models import Project
from api.user.serializers import UserSerializer
from django.db import models

# dict_user = {
#     'username' : 'sangh',
#     'password' : '123', 
#     # 'confirm_password' : '123',
#     'first_name' : 'Nguyen'
    
# # }
# user =  User.objects.get(username = 'admin')

# data =  UserSerializer(user)

# print(data.data)


# a = RolePermission.objects.annotate(user = models.F('role_id__role_id__user_id'),
#                                             codename = models.F('permission_id__codename')).get(user =2,
#                                                                                             codename = 'add_user')

# print(a)

# for i in a:
    
#     print(i.codename)



