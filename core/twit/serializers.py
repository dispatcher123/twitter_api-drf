from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile,Twitter,Comment






class CommentSerializer(serializers.ModelSerializer):
    profiles=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Comment
        # fields='__all__'
        fields=[
            'id',
            'comment',
            'created_date',
            'updated_date',
            'profiles'
            
            
        ]

class TwitterSerializer(serializers.ModelSerializer):
    twitter_comment=CommentSerializer(many=True,read_only=True)
    profile_user=serializers.StringRelatedField(read_only=True)
    views=serializers.StringRelatedField(read_only=True)
    total_comment = serializers.IntegerField(source='twitter_comment.count', read_only=True)
    class Meta:
        model=Twitter
        fields=(
            'id',
            'updated_date',
            'profile_user',
            'twit',
            'total_comment',
            'views',
            'twitter_comment',
            
            
        )



class ProfileSerializer(serializers.ModelSerializer):
    twitters=TwitterSerializer(many=True,source='twitter_user', read_only=True)
    user=serializers.StringRelatedField(read_only=True)
    total_twitter = serializers.IntegerField(source='twitter_user.count', read_only=True)
    class Meta:
        model=Profile
        fields=(
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'bio',
            'status',
            'city',
            'age',
            'updated_date',
            'user',
            'total_twitter',
            'twitters',
            

        )
