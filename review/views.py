from rest_framework.viewsets import ModelViewSet
from blog.models import Event,ReviewComment,Role
from blog.renderers import CustomRenderer
from .models import EventReviewers
from .serializers import EventReviewersSerializer,EventSerializer,FetchEventReviewersSerializer,FetchReviewerEventCountSerializer
from blog.serializers import AdminTitleSerializer, AuthorTitleSerializer, ReviewCommentSerializer, ReviewerTitleSerializer, RoleSerializer,ContentWriterTitleSerializer,UserTitleSerializer,UserEventSerializer,AdminEventSerializer,ReviewerEventSerializer,ContentWriterEventSerializer,AuthorEventSerializer
from blog.permissions import IsAdmin,IsAuthor,IsContentWriter,IsReviewer,IsUser
from blog.functions import get_user_role
from blog.classes import StandardResponse
from rest_framework import status
from rest_framework.decorators import permission_classes
import rest_framework
from rest_framework.views import APIView
from django.db.models import Count


# To get list of events assigned to particular reviewer
class ReviewerAssignedEventsViewSet(ModelViewSet):
    http_method_names = ['get','post','put','patch']
    renderer_classes = [CustomRenderer]
    permission_classes = [IsReviewer]
    def get_queryset(self):
        reviewer_id = self.request.user.id
        assigned_event_ids = EventReviewers.objects.values('event_id').filter(assigned_reviewer_id=reviewer_id)
        return Event.objects.filter(id__in=assigned_event_ids).all()
    serializer_class = EventSerializer

# To post comments on an event
class ReviewerCommentsViewSet(ModelViewSet):
    renderer_classes = [CustomRenderer]
    permission_classes = [IsReviewer]
    def get_queryset(self):
        reviewer_id = self.request.user.id
        assigned_event_ids = EventReviewers.objects.values('event_id').filter(assigned_reviewer_id=reviewer_id)
        return ReviewComment.objects.filter(event_id__in=assigned_event_ids).all()
    serializer_class = ReviewCommentSerializer
      
    
# To get List of events authored by him which have status "Under Review" 
class AuthorViewSet(ModelViewSet):
    http_method_names = ['get','post']
    def get_queryset(self):
        author_id = self.request.user.id
        return Event.objects.filter(author_id=author_id,status='U')
    serializer_class = AuthorEventSerializer
    permission_classes = [IsAuthor]
    renderer_classes = [CustomRenderer]
        
@permission_classes([rest_framework.permissions.IsAuthenticated,IsAdmin])
class AssignReviewer(APIView):
    def post(self,request,format="json"):
        role = Role.objects.filter(account_id=self.request.data.get("reviewer_id"),is_reviewer=1)            
        if len(role)>0:
            count = EventReviewers.objects.filter(assigned_reviewer_id=self.request.data.get("reviewer_id"),archived=0)
            if len(count)<10 :
                event = Event.objects.filter(id=self.request.data.get("event_id"))
                if len(event) > 0:
                    event = event[0]
                    eventreviewers = EventReviewers.objects.filter(event_id=self.request.data.get("event_id"),archived=0)
                    if len(eventreviewers)>0:
                        eventreviewers = eventreviewers[0]
                        if eventreviewers.assigned_reviewer_id == self.request.data.get("reviewer_id"):
                            return StandardResponse.success_response(self,data = {"":""},message="The revivwer for particular event is already exits",status=status.HTTP_200_OK)
                        eventreviewers.archived = 1
                        eventreviewers.save()

                    eventreviewers = EventReviewers(event_id_id=event.id,assigned_reviewer_id_id=self.request.data.get("reviewer_id"),author_id=event.author_id)
                    eventreviewers.save()
                    event.status = "U"
                    event.save()
                    return StandardResponse.success_response(self,data = {"":""},message="Reviwer assigned Succesfully",status=status.HTTP_200_OK)
                return StandardResponse.success_response(self,data = {"":""},message="Wrong event id",status=status.HTTP_400_BAD_REQUEST)
            return StandardResponse.success_response(self,data = {"":""},message="Revivwer already have 10 events assigned",status=status.HTTP_400_BAD_REQUEST)
        return StandardResponse.success_response(self,data = {"":""},message="Please Enter Valid Reviwer",status=status.HTTP_400_BAD_REQUEST)


@permission_classes([rest_framework.permissions.IsAuthenticated,IsReviewer])
class FetchReviewerEvent(APIView):
    def get(self,request,format="json"):
        eventreviewers = EventReviewers.objects.filter(assigned_reviewer_id = request.user.id)

        data = FetchEventReviewersSerializer(eventreviewers,many=True).data
        return StandardResponse.success_response(self,data = data,message="Reviwer event succesfully",status=status.HTTP_200_OK)
    
@permission_classes([rest_framework.permissions.IsAuthenticated,IsAdmin])
class FetchReviewerEventCount(APIView):
    def get(self,request,format="json"):
        data = EventReviewers.objects.filter(archived=0).values('assigned_reviewer_id').annotate(total=Count('event_id'))
        data = FetchReviewerEventCountSerializer(data,many=True).data
        return StandardResponse.success_response(self,data = data ,message="Please Enter Valid Reviwer",status=status.HTTP_200_OK)