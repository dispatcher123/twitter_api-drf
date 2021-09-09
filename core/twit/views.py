from django.shortcuts import render
from rest_framework.generics import CreateAPIView, get_object_or_404
from .serializers import ProfileSerializer,TwitterSerializer,CommentSerializer
from .models import Profile,Twitter,Comment
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework import mixins
from .permissions import UpdataProfile,UpdateTwitter
from rest_framework.response import Response
from django.db.models import F
# Create your views here.


class ProfileList(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = Profile.objects.all().order_by('-id')
    serializer_class=ProfileSerializer
    permission_classes = [IsAuthenticated,UpdataProfile]


    def perform_create(self, serializer):
        profile_user = self.request.user.profile
        serializer.save(profile_user=profile_user)




class TwitterList(ModelViewSet):
    queryset=Twitter.objects.all().order_by('-id')
    serializer_class=TwitterSerializer
    permission_classes = [IsAuthenticated,UpdateTwitter]

    def perform_create(self, serializer):
        profile_user = self.request.user.profile
        serializer.save(profile_user=profile_user)

    # created by RetrieveModelMixin 
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Twitter.objects.filter(pk=instance.id).update(views=F('views') + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)




# class TwitterDetail(RetrieveAPIView):
#     queryset=Twitter.objects.all().order_by('-id')
#     serializer_class=TwitterSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         tweet_pk=self.kwargs.get('tweet_pk')
#         twitter=get_object_or_404(Twitter, pk=tweet_pk)
#         serializer.save(twitter=twitter)
        
# class TwitterCreate(CreateAPIView):
#     queryset=Twitter.objects.all().order_by('-id')
#     serializer_class=TwitterSerializer
#     permission_classes = [IsAuthenticated,UpdateTwitter]

#     def perform_create(self, serializer):
#         profile_user = self.request.user.profile
#         serializer.save(profile_user=profile_user)


class CommentCreate(CreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        tweet_pk=self.kwargs.get('pk')
        twitter=get_object_or_404(Twitter, pk=tweet_pk)
        profile_id=self.request.user
        profiles=get_object_or_404(Profile, user_id=profile_id)
        serializer.save(twitter=twitter,profiles=profiles)


    