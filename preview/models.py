from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)

    def get_info(self):
        return {
            'email': self.user.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'company': self.company,
        }

    def __str__(self):
        return str(self.user)


    def update(self, email, first_name, last_name, company):
        self.user.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.company = company

        self.user.save()
        self.save()
