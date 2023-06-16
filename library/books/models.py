from django.db import models
from uuid import uuid4

# Create your models here.

class Books(models.Model):
    idBook = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    releaseYear = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)

from django.conf import settings  
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token 

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

