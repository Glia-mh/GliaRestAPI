from django.shortcuts import render
from rest_framework import generics
from database.models import GliaUser, GliaCounselor, GliaConversation
from database.serializers import GliaUserSerializer, GliaCounselorSerializer, GliaConversationSerializer

# Create your views here.

# ----------- USER VIEWS ------------------- #
class UserList(generics.ListCreateAPIView):
    queryset = GliaUser.objects.all()
    serializer_class = GliaUserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = queryset = GliaUser.objects.all()
    lookup_field = "gliaID"
    serializer_class = GliaUserSerializer



# ------------- COUNSELOR VIEWS --------------- #
class CounselorList(generics.ListCreateAPIView):
    queryset = GliaCounselor.objects.all()
    serializer_class = GliaCounselorSerializer

class CounselorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GliaCounselor.objects.all()
    serializer_class = GliaCounselorSerializer



# -------------- CONVERSATION VIEWS ------------ #
class ConversationList(generics.ListCreateAPIView):
    queryset = GliaConversation.objects.all()
    serializer_class = GliaCounselorSerializer

class ConversationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GliaConversation.objects.all()
    lookup_field = 'conversationID'
    serializer_class = GliaConversationSerializer
