import binascii
from datetime import date
import os
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.contrib.auth.hashers import check_password, make_password
from django.utils import timezone
from app.views.models import UserRolePermission

class User(AbstractUser):
    position_role = models.IntegerField(blank=True, null=True)
    
    rank = models.CharField(max_length=100)


    token = models.CharField(max_length=200, db_column='account_token', blank=True, null=True, verbose_name='Token')
    token_date = models.DateField(db_column='account_token_date', blank=True, null=True, verbose_name=('Token Date'))
    # Reset
    account_token_reset_pass = models.CharField(max_length=200, db_column='account_token_reset_pass',
                                                blank=True, null=True)
    account_token_reset_pass_time = models.DateTimeField(db_column='account_token_reset_pass_time',
                                                         blank=True, null=True)

    def __str__(self):
        return self.username


    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_key()
            self.token_date = date.today()
        return super().save(*args, **kwargs)

    @property
    def is_authenticated(self):
        return True

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    @property
    def get_key(self):
        import base64

        key = '{}:{}'.format(self.id, self.token)
        key = key.encode()

        try:
            return base64.b64encode(key).decode('utf-8')
        except:
            return None

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def reset_key(self, _date):
        if self.token_date != _date:
            self.token_date = _date
            self.token = self.generate_key()
            self.save()

        return self.get_key

    def update_last_login(self):
        self.last_login = timezone.now()
        self.save(update_fields=['last_login'])

    def verify_permission(self, codename):
        if self.is_superuser == False:
            permission =  UserRolePermission.objects.filter(user_id=self.id, permission_codename=codename).values('permission_codename') 
            if not permission:
                return False
        return True

    