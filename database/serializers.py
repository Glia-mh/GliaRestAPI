from database.models import GliaUser, GliaCounselor, GliaConversation
from rest_framework import serializers
from django.contrib.auth.models import User

class GliaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GliaUser
        fields = ('id','username','conversationID','progress','phqResponses')

class GliaCounselorSerializer(serializers.ModelSerializer):
   # conversations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = GliaCounselor
        fields = ('id','counselorName','counselorBio','counselorImageURL')

class GliaConversationSerializer(serializers.ModelSerializer):
    counselor = GliaCounselorSerializer()
    class Meta:
        model = GliaConversation
        fields = ('id','conversationTitle','counselor')