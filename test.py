import os
from tokenize import Pointfloat
from turtle import position

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rating_employee.settings')


django.setup()

from core.user.models import User,RolePermission, UserRole
from core.group_skill.models import Skill
from core.project.models import Project
from core.rating.models import Rating
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



# a = UserRole.objects.annotate(user_role_id  = models.F('user_id__id'),
#                                       priority = models.F('role_id__priority')).get(
#                                           user_role_id = 2
#                                       )
# print(a.priority)

# list_user = User.objects.filter(position='API').values_list('id')
# ratings = Rating.objects.filter(user_id_rated_id__in = list_user)
# # print('rating: ', rating)
# for rating in ratings:
#     print(f'{rating.id}, {rating.user_id_rated}')

# a =  ['D','C','B','A','S']

# print(a.index('d'))
# print(True or False)/

skill = Skill.objects.annotate(
                skill_name=models.F('name'),
                group_skill_name=models.F('group_skill_id__group_skill_name'),
            ).get(id=2).field(
                'id',
                'skill_name',
                'group_skill_name',
            )
print(type(skill))