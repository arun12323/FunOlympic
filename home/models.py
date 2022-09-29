from django.db import models
from django.contrib.auth.models import User
from accounts.models import Country

class UserCountry(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_countries'
        verbose_name = 'User Country'
        verbose_name_plural = 'User Country'

    def __str__(self):
        return self.account.username