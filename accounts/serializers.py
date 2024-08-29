from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import Room,Topic,Message
from django.contrib.humanize.templatetags.humanize import naturaltime
import base64
from django.contrib.auth import get_user_model
User = get_user_model()

class Base64BinaryField(serializers.Field):
    def to_representation(self, value):
        if value:
            return base64.b64encode(value).decode('utf-8')
        return None

    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            # Remove the metadata header
            _, imgstr = data.split(';base64,') 
            # Decode the base64 string into binary data
            return base64.b64decode(imgstr)
        raise serializers.ValidationError("Invalid image format.")

class UserCreateSerializer(UserCreateSerializer):
    avatar = Base64BinaryField(required=False)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'full_name', 'user_name', 'password', 'bio', 'department', 'avatar', 'total_points']

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id','name']

class RoomSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()
    host = UserCreateSerializer(read_only=True)
    participants = UserCreateSerializer(many=True, read_only=True)
    time_since_created = serializers.SerializerMethodField()
    participant_count = serializers.SerializerMethodField()
    class Meta:
        model = Room
        fields = ['id','host','name','topic','description','created','updated','participants','participant_count','time_since_created']

    def get_time_since_created(self, obj):
        return naturaltime(obj.created)

    def get_participant_count(self, obj):
        return obj.participants.count()

class MessageSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer(read_only=True)
    room = RoomSerializer()
    time_since_updated = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['id','user','room','body','updated','created','time_since_updated']

    def get_time_since_updated(self, obj):
        return naturaltime(obj.updated)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'user_name','bio','department', 'avatar','total_points')

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'user_name','bio','department', 'avatar','total_points')



 

    
