from django.db import models
from django.contrib.auth.models import User

class Userprofile(models.Model):
    # A user can only have one profile
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)

    def __str__(self):
        # allows us to get the username instead of an object
        return self.user.username