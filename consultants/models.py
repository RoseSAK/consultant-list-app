from django.db import models
from django.contrib.auth.models import User

def is_manager(user):
    return user.groups.filter(name='Manager').exists()

class Consultant(models.Model):

    TECHNOLOGY_CONSULTING = 'TC'
    SOFTWARE_ENGINEERING = 'SE'
    DELIVERY = 'D'
    CORPORATE = 'C'
    PRACTICE_CHOICES = (
        (TECHNOLOGY_CONSULTING, 'Technology Consulting'),
        (SOFTWARE_ENGINEERING, 'Software Engineering'),
        (DELIVERY, 'Delivery'),
        (CORPORATE, 'Corporate'),
    )

    consultant_name = models.CharField(max_length=150, blank=False)
    contact_number = models.CharField(max_length=200, blank=True, null=True)
    practice = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    role = models.CharField(max_length=200, blank=True, null=True)
    teams = models.CharField(max_length=200, blank=True, null=True)
    skills = models.CharField(max_length=200, blank=True, null=True)
    sectors = models.CharField(max_length=200, blank=True, null=True)
    notes = models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return u"{0}".format(self.consultant_name)


