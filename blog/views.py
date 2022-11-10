from rest_framework.viewsets import ModelViewSet
from blog.renderers import CustomRenderer
from .models import Event, ReviewComment, Role, Title
from blog.serializers import AdminTitleSerializer, AuthorTitleSerializer, ReviewCommentSerializer, ReviewerTitleSerializer, RoleSerializer,ContentWriterTitleSerializer,UserTitleSerializer,UserEventSerializer,AdminEventSerializer,ReviewerEventSerializer,ContentWriterEventSerializer,AuthorEventSerializer,BlogSerializer
from .permissions import IsAdmin,IsAuthor,IsContentWriter,IsReviewer,IsUser
from blog.functions import get_user_role
from blog.classes import StandardResponse
from rest_framework import status
from rest_framework.decorators import permission_classes
import rest_framework
from rest_framework.views import APIView
from api.models import Account


class TitleViewSet(ModelViewSet):
    renderer_classes = [CustomRenderer]
    queryset = Title.objects.all()
    def get_serializer_class(self):
        role = get_user_role(self)
        if role == 'admin':
            return AdminTitleSerializer
        elif role == 'reviewer':
            return ReviewerTitleSerializer
        elif role == 'content writer':
            return ContentWriterTitleSerializer
        elif role == 'author':
            return AuthorTitleSerializer
        elif role == 'user':
            return UserTitleSerializer

    def get_permissions(self):
        role = get_user_role(self)
        if role == 'admin':
            return [IsAdmin()]
        elif role == 'reviewer':
            return [IsReviewer()]
        elif role == 'author':
            return [IsAuthor()]
        elif role == 'content writer':
            return [IsContentWriter()]
        elif role == 'user':
            return [IsUser()]
    
    def get_serializer_context(self):
        try:
            title_id = self.kwargs['title_pk']
        except KeyError:
            title_id = None
        return {'account_id':self.request.user.id,'title_id':title_id}
        
class EventViewSet(ModelViewSet):
    renderer_classes = [CustomRenderer]
    def get_queryset(self):
        user_id = self.request.user.id
        try:
            title_id = self.kwargs['title_pk']
        except KeyError:
            title_id = None
        role = get_user_role(self)
        if role == 'user':
            return Event.objects.filter(title_id=title_id,status='A').all()
        elif role == 'author':
            return Event.objects.filter(title_id=title_id,author_id=user_id).all()
        elif title_id == None:
            return Event.objects.all()
        return Event.objects.filter(title_id=title_id).all()
        
    def get_serializer_class(self):
        role = get_user_role(self)
        if role == 'admin':
            return AdminEventSerializer
        elif role == 'reviewer':
            return ReviewerEventSerializer
        elif role == 'content writer':
            return ContentWriterEventSerializer
        elif role == 'author':
            return AuthorEventSerializer
        elif role == 'user':
            return UserEventSerializer
    
    def get_permissions(self):
        role = get_user_role(self)
        if role == 'admin':
            return [IsAdmin()]
        elif role == 'reviewer':
            return [IsReviewer()]
        elif role == 'author':
            return [IsAuthor()]
        elif role == 'content writer':
            return [IsContentWriter()]
        elif role == 'user':
            return [IsUser()]
    
    def get_serializer_context(self):
        try:
            title_id = self.kwargs['title_pk']
        except KeyError:
            title_id = None
        return {'author_id':self.request.user.id,'title_id':title_id}
    
class ReviewCommentViewSet(ModelViewSet):
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer
    permission_classes = [IsReviewer]

class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAdmin]

@permission_classes([rest_framework.permissions.IsAuthenticated,])
class AuthorView(APIView):

    def get(self,request,format="json"):

        event = Event.objects.filter(id=self.request.data.get("event_id"))

        if event[0].validation(request.user.id):
            return StandardResponse.success_response(self,data = {"HI":"HI"},message="Data Fetched Successfully!",status=status.HTTP_200_OK)
        return StandardResponse.success_response(self,data = {"":""},message="Data Not Fetched Successfully!",status=status.HTTP_200_OK)

@permission_classes([rest_framework.permissions.IsAuthenticated,])
class FetchAllBlog(APIView):
    def get(self,request,format="json"):
        account = Account.objects.filter(id=self.request.data.get("id"))
        if not account.exists():
            return StandardResponse.success_response(self,data = {"":""},message="User not Found",status=status.HTTP_200_OK)

        blog = BlogSerializer(account[0]).data
        return StandardResponse.success_response(self,data = blog,message="Users Event Title wise fetched successfully!",status=status.HTTP_200_OK)