from django.db import models

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

class Users(models.Model):
    #id is auto generated
    password_hash = models.CharField(max_length=60)
    auth_token = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    def __str__(self):
        return self.id

class Groups(models.Model):
    #id is auto generated
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)
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
