from django.shortcuts import render
from rest_framework import generics
from database.models import GliaUser, GliaCounselor, GliaConversation
from database.serializers import GliaUserSerializer, GliaCounselorSerializer, GliaConversationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from database.permissions import GliaPermissions, GliaGetPermission
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = GliaConversationSerializer



# ------ create user ----- # 
class CreateGliaUser(generics.ListCreateAPIView):
    queryset = GliaUser.objects.all()
    permission_classes = (GliaPermissions,)
    serializer_class = GliaUserSerializer


    def perform_create(self, serializer):
        conversationID = GliaUser.objects.count() // 4 + 1 
        serializer.save(conversationID=conversationID)

    #TODO: Add update for phq9

# -------------- Summarizer Endpoints ----------- #
class Statistics(APIView):

    def get(self, request, format=None):
        user_count = GliaUser.objects.count()
        conversation_count = GliaConversation.objects.count()
        data = {'userCount':user_count, 'conversationCount': conversation_count }
        return Response(data)

# ---- get conversationID ---- #

class GetUserConversation(APIView):
    permission_classes = (GliaGetPermission,)

    def get(self,request, format=None):
        username = request.query_params['username']
        user = get_object_or_404(GliaUser, username=username)
        return Response(({'conversationID' : user.conversationID}))
    
    # ----- update phq9 responses ---- #
    def put(self, request,format=None):
        username = request.query_params['username']
        print(username)
        user = get_object_or_404(GliaUser, username=username)
        phq9 = request.query_params['phq9']
        print(phq9)
        user.phqResponses = phq9
        user.save()
        return Response({'status':'success'})

    



