from django.db import models


class Tweet(models.Model):
    """
    Poor Man's Tweet model
    """
    # according to requirement, tweet content is limited to 50 characters
    content = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    created_dt = models.DateTimeField(auto_now=True)
        