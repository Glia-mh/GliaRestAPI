from django.db import models
import uuid

# Create your models here.


class GliaUser(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    gliaID = models.CharField(max_length=100)
    conversationID = models.IntegerField()
    progress = models.IntegerField() # Should be a value between 0 - 100

    class Meta:
        ordering = ('created',)

class GliaCounselor(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    counselorID = models.UUIDField(editable=False, default=uuid.uuid4)
    counselorName = models.CharField(max_length=100)
    counselorBio = models.TextField() # Should be a description for a counselor 
    counselorImageURL = models.CharField(max_length=200)

    class Meta:
        ordering = ('created',)

class GliaConversation(models.Model):

     created = models.DateTimeField(auto_now_add=True) # just ensures ordered by creation
     conversationID = models.IntegerField() # Sequentially order 1 .... n 
     conversationTitle = models.CharField(max_length=200) 
     counselorID = models.IntegerField() # reference to GliaCounselor

     class Meta: 
         ordering = ('created',)



