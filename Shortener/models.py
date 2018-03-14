from django.db import models


class NewAdress(models.Model):
    main_url = models.CharField(max_length=1000)
