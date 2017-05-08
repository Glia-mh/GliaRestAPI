from database.models import GliaUser, GliaCounselor, GliaConversation
from rest_framework import serializers

class GliaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GliaUser
        fields = ('id', 'gliaID','conversationID','progress')

class GliaCounselorSerializer(serializers.ModelSerializer):
    class Meta:
        model = GliaCounselor
        fields = ('id','counselorName','counselorBio','counselorImageURL')

class GliaConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GliaConversation
        fields = ('id','conversationID','conversationTitle','counselorName')