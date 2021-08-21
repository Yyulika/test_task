
from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField("Наименование", max_length=30)
    description = models.CharField("Описание", max_length=30)
    parameters = models.JSONField("Параметры", null=True)

    def __str__(self):
        return self.title
