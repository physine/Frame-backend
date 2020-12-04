from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Django will create a table like so with each of the models 
# CREATE TABLE exaple_table (
#     "id" serial NOT NULL PRIMARY KEY,
#     "first_name" varchar(30) NOT NULL,
#     "last_name" varchar(30) NOT NULL
#     .
#     .
#     .
#     ect
# );
#
# By default, Django gives each model the following field:
#
# id = models.AutoField(primary_key=True)

#TODO: will need a reset password code table

# class Users(models.Model):
#     password_hash = models.CharField(max_length=60)
#     #auth_token = models.CharField(max_length=60)
#     email = models.CharField(unique=True, max_length=60)
#     first_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)

#     # def __str__(self):
#     #     return self.id



class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            return ValueError('users must have an email')
        if not username:
            return ValueError('users must have an username')
        if not password:
            return ValueError('users must have an password')

        user = self.model(
            email=self.normalize_email(email), # convert to lowercase
            username = username,
            password=password,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email), # convert to lowercase
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser):
    # required fields
    email        = models.EmailField(verbose_name='email', unique=True, max_length=60)
    username     = models.CharField(max_length=60)
    date_joined  = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login   = models.DateTimeField(verbose_name='last login', auto_now_add=True)
    is_admin     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff     = models.BooleanField(default=False)

    # used to login
    USERNAME_FIELD = 'email'
    # requried when reg
    REQUIRED_FIELDS = ['username',]

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, perm, obj=None):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_name(self, app_lable):
        return True


    
    


class AuthToken(models.Model):
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=60)

class Groups(models.Model):
    #id is auto generated
    users_id = models.OneToOneField(Users, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=60)

class UsersGroups(models.Model):
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    groups_id = models.ForeignKey(Groups, on_delete=models.CASCADE)

class Images(models.Model):
    #id is auto generated
    image_name = models.CharField(max_length=60)

class UserImages(models.Model):
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    images_id = models.ForeignKey(Images, on_delete=models.CASCADE)

class GroupImages(models.Model):
    groups_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    images_id = models.ForeignKey(Images, on_delete=models.CASCADE)

class Friends(models.Model):
    # when all the friends of a user want to be found the id of that user will be
    # found in the lookup_id field and for all the rows it exists in the results_id of thoses rows are returned; finding tall the friends of that user.
    lookup_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    results_id = models.IntegerField()

class ResetPasswordCode(models.Model):
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    # there can be more than one reset password code at a gives time 
    reset_code = models.IntegerField() 