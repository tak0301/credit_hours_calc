import datetime

from django.db import models
from django.utils import timezone

class Activity(models.Model):
    Contact = 'Contact Time'
    Independent = 'Independent Learning'
    activity_type_choices = (
        (Contact, 'Contact Time'),
        (Independent, 'Independent Learning')
    )
    activity_type = models.CharField(max_length=200, choices=activity_type_choices, default=Contact)
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()
    image = models.FileField(default='No activity image')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.activity_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
