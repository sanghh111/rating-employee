import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rating_employee.settings')


django.setup()

from core.user.models import User
from api.user.serializers import UserSerializer


# dict_user = {
#     'username' : 'sangh',
#     'password' : '123', 
#     # 'confirm_password' : '123',
#     'first_name' : 'Nguyen'
    
# # }
# user =  User.objects.get(username = 'admin')

# data =  UserSerializer(user)

# print(data.data)


a = {
    'n' :12
}

a['b']