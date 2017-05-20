from django.db import models
import uuid
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.validators import validate_comma_separated_integer_list
from django.conf import settings
from rest_framework.authtoken.models import Token
# Create your models here.


class GliaUser(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    conversationID = models.IntegerField(null=True)
    username = models.CharField(max_length=200, unique=True)
    progress = models.IntegerField() # Should be a value between 0 - 100
    phqResponses = models.CharField(blank=True, max_length=100)


    def __str__(self):
        return self.username
    

    class Meta:
        ordering = ('created',)

class GliaCounselor(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    counselorName = models.CharField(max_length=100)
    counselorBio = models.TextField() # Should be a description for a counselor 
    counselorImageURL = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=User)
    def create_counselor_profile(sender, instance, created, **kwargs):
        print(kwargs)
        if created:
            GliaCounselor.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    class Meta:
        ordering = ('created',)

class GliaConversation(models.Model):
     created = models.DateTimeField(auto_now_add=True) # just ensures ordered by creation
     conversationTitle = models.CharField(max_length=200) 
     counselor = models.ForeignKey(GliaCounselor, null=True, related_name='conversations',on_delete=models.SET_NULL) # reference to GliaCounselor

     class Meta: 
         ordering = ('created',)
     def __str__(self):
         return self.conversationTitle



