from rest_framework import serializers
from .models import ReviewComment, Role, Title, Event
from api.models import Account

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['title','country_of_origin']


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id','author_id','description','year','status']

class EventPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title_id','author_id','description','year']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class ReviewCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewComment
        fields = '__all__'

class UserTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Title
        fields = ['id', 'title']

class UserEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id','title_id','description']

class AdminTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

class AdminEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ReviewerTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = '__all__'

class ReviewerEventSerializer(serializers.ModelSerializer):
    comments = ReviewCommentSerializer(many=True)
    class Meta:
        model = Event
        fields = ['id','title_id','author','description','year','created_at','status','comments']
    
class ContentWriterTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['id','title']
class ContentWriterEventSerializer(serializers.ModelSerializer):
    # title_id = serializers.CharField(read_only=True)
    class Meta:
        model = Event
        fields = ['title_id','description']

class AuthorTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['id','title']
    
class AuthorEventSerializer(serializers.ModelSerializer):   
    status = serializers.CharField(read_only=True)
    comments = ReviewCommentSerializer(many=True,read_only=True)
    class Meta:
        model = Event
        fields = ['id','title_id','author_id','description','year','status','comments']


class BlogSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    class Meta:
        model = Account
        fields = ('id','first_name','last_name','middle_name','email','phone','gender','title')
    def get_title(self,obj):
        title = Title.objects.filter(events__author_id=obj.id).distinct()
        event = TitleEventSerializer(title,many=True,context={'id': obj.id}).data
        return event


class TitleEventSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    event = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = ['title','event']
    def get_title(self,obj):
        return obj.title
    def get_event(self,obj):
        event = Event.objects.filter(title_id = obj.id,author_id = self.context.get('id') )
        event = EventListSerializer(event,many=True).data
        return event

