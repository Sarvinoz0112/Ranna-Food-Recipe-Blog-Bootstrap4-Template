from django.db import models


class UserFormModel(models.Model):
    file = models.FileField()
