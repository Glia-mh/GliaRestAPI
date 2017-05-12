from django.shortcuts import render
from rest_framework import generics
from database.models import GliaUser, GliaCounselor, GliaConversation
from database.serializers import GliaUserSerializer, GliaCounselorSerializer, GliaConversationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
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
    lookup_field='counselorID'
    serializer_class = GliaCounselorSerializer



# -------------- CONVERSATION VIEWS ------------ #
class ConversationList(generics.ListCreateAPIView):
    queryset = GliaConversation.objects.all()
    serializer_class = GliaConversationSerializer

class ConversationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GliaConversation.objects.all()
    lookup_field = 'conversationID'
    serializer_class = GliaConversationSerializer


# -------------- Summarizer Endpoints ----------- #
class Statistics(APIView):

    def get(self, request, format=None):
        user_count = GliaUser.objects.count()
        conversation_count = GliaConversation.objects.count()
        data = {'userCount':user_count, 'conversationCount': conversation_count }
        return Response(data)