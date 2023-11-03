from django.db import models

class User(models.Model):
    """A class to represent single item"""
    user_id = models.AutoField(primary_key=True)
    user_nickname = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    user_surname = models.CharField(max_length=30)
    user_e_mail = models.EmailField(max_length=50)
    user_password = models.CharField(max_length=30)
    date_of_birth = models.DateField()