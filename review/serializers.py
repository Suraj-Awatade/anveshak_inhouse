from rest_framework import serializers
from api.models import Account
from blog.models import Event,Title,ReviewComment,Role
from .models import EventReviewers
from blog.serializers import EventListSerializer,EventPostSerializer
from django.db.models import Count

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id','title_id','author_id','description','year','created_at','status']
class EventReviewersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventReviewers
        fields = '__all__'

class FetchEventReviewersSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    event = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ['title','event']
        # fields = ['event']

    def get_title(self,obj):
        event = Event.objects.filter(id = obj.event_id)
        title = Title.objects.filter(id = event[0].title_id_id)
        return title[0].title

    def get_event(self,obj):
        event = Event.objects.filter(id = obj.event_id)
        event = EventListSerializer(event[0]).data
        return event

class FetchReviewerEventCountSerializer(serializers.ModelSerializer):
    assigned_reviewer_id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()
    approved = serializers.SerializerMethodField()
    rejected = serializers.SerializerMethodField()
    
    class Meta:
        model = Event
        fields = ['assigned_reviewer_id','name','total','approved','rejected']
        
    def get_name(self,obj):
        account = Account.objects.filter(id=obj.get('assigned_reviewer_id'))
        return " ".join([account[0].first_name,account[0].last_name])

    def get_assigned_reviewer_id(self,obj):
        return obj.get('assigned_reviewer_id')
    
    def get_total(self,obj):
        dict = {}
        dict['total'] = obj.get('total')

        a = EventReviewers.objects.filter(archived=0,assigned_reviewer_id = obj.get('assigned_reviewer_id')).filter(event__status = 'U').values('event_id').annotate(Count('event_id'))

        if len(a) > 0:
            dict['Under Review'] = a[0].get('event_id__count')
        else:
            dict['Under Review'] = 0

        # a = EventReviewers.objects.filter(archived=0,assigned_reviewer_id = obj.get('assigned_reviewer_id')).filter(event__status = 'RW').values('event_id').annotate(Count('event_id'))
        # if len(a) > 0:
        #     dict['Rework'] = a[0].get('event_id__count')
        # else:
        #     dict['Rework'] = 0
            
        return dict
    
    def get_approved(self,obj):
        dict = {}
        a = EventReviewers.objects.filter(archived=0,assigned_reviewer_id = obj.get('assigned_reviewer_id')).filter(event__status = 'A').values('event_id').annotate(Count('event_id'))
        if len(a) > 0:
                return a[0].get('event_id__count')
        return 0
    
    def get_rejected(self,obj):
        a = EventReviewers.objects.filter(archived=0,assigned_reviewer_id = obj.get('assigned_reviewer_id')).filter(event__status = 'R').values('event_id').annotate(Count('event_id'))
        if len(a) > 0:
                return a[0].get('event_id__count')
        return 0