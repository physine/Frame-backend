from django.db import models

# TODO: create db table ForeignKey fields where needed

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    password_hash = models.CharField(max_length=60)
    auth_token = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    def __str__(self):
        return self.UID

class UsersGroups(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=60)


class Groups(models.Model):
    group_id = models.AutoField(primary_key=True)

class UserImages(models.Model):
    pass

class Images(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_name = models.CharField(max_length=60)

class GoupImages(models.Model):
    pass

class Friends(models.Model):
    pass


