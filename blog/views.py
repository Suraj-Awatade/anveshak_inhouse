from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from blog.renderers import CustomRenderer
from .models import Event, ReviewComment, Role, Title
from blog.serializers import (AdminTitleSerializer, AuthorTitleSerializer, ReviewCommentSerializer, 
                              ReviewerTitleSerializer, RoleSerializer,ContentWriterTitleSerializer,
                              UserTitleSerializer,UserEventSerializer,AdminEventSerializer,
                              ReviewerEventSerializer,ContentWriterEventSerializer,
                              AuthorEventSerializer,BlogSerializer,UsersRoleWiseSerializer,EventsTitleWiseSerializer)
from .permissions import IsAdmin,IsAuthor,IsContentWriter,IsReviewer,IsUser
from blog.functions import get_user_role
from blog.classes import StandardResponse
from rest_framework import status
from rest_framework.decorators import permission_classes
import rest_framework
from rest_framework.views import APIView
from api.models import Account
from api.serializers import SignUpSerializer
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import F
from api.pagination import CustomPageNumberPagination  


class TitleViewSet(ModelViewSet):
    renderer_classes = [CustomRenderer]
    queryset = Title.objects.all()
    pagination_class=CustomPageNumberPagination
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
    pagination_class=CustomPageNumberPagination

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
    pagination_class=CustomPageNumberPagination
    permission_classes = [IsReviewer]

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
        return StandardResponse.success_response(self,data = blog,message="Users event Title wise fetched successfully!",status=status.HTTP_200_OK)
    
    

class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    pagination_class=CustomPageNumberPagination
    permission_classes = [IsAdmin]


class AdminAddUser(ModelViewSet):
    renderer_classes = [CustomRenderer]
    queryset = Account.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [IsAdmin]
    
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def send_registration_mail(sender,instance=None,created=False,**kwargs):
    if created:
        new_line='\n'
        subject = f'Hi {instance.first_name} {instance.last_name}!!! WELCOME to ANVESHAK_INHOUSE. Your Account is Created by Admin.'
        message = f'Thank you for registering.{new_line}Your Login Credentials are: {new_line}email={instance.email} {new_line}password={instance._password}.{new_line}Do not share your password with anyone.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email, ]
        send_mail(subject, message, email_from, recipient_list)
   
   
# class RolewiseUsers(APIView):
    # def get(self,request,format="json"):
    #     account = Account.objects.filter(id=self.request.data.get("id"))
    #     if not account.exists():
    #         return StandardResponse.success_response(self,data = {"":""},message="User not Found",status=status.HTTP_200_OK)

    #     blog = BlogSerializer(account[0]).data
    #     return StandardResponse.success_response(self,data = blog,message="Users event Title wise fetched successfully!",status=status.HTTP_200_OK)
        
        
@permission_classes([IsAdmin,])  
class UsersRoleWise(APIView):
    
    def get(self,request):
        return Response({'msg':'Get Request'})
    
    def post(self,request):
        serializer = UsersRoleWiseSerializer(data=request.data)
        data = {}
        serializer.is_valid()
        user_input=request.data['user_input']

        if user_input=='admin':
            role_users = Role.objects.filter(is_admin=1).values('id')
        elif user_input=='author':
            role_users = Role.objects.filter(is_author=1).values('id')
            print(role_users)
        elif user_input=='reviewer':
            role_users = Role.objects.filter(is_reviewer=1).values('id')
        elif user_input=='content_writer':
            role_users = Role.objects.filter(is_content_writer=1).values('id')
        elif user_input=='user':
            role_users = Role.objects.filter(is_user=1).values('id')
        else:
            return Response({'error':'Input Not Valid.Enter Valid Role'})
        
        my_dict = []
        for item in role_users:
            user_name= Account.objects.filter(roles__account_id=item['id']).values('id','first_name','last_name','dob','phone','roles').annotate(account_id = F('roles__account_id'))
            my_dict.append(user_name[0])
            
        if serializer.is_valid():
            data['response'] = "Successfully Fetched data"
            data['my_dict'] = my_dict
        else:
            data = serializer.errors
            
        return Response(data)

class EventsTitleWise(APIView):
    pagination_class=CustomPageNumberPagination
    def get(self, request, format=None):
        user = Title.objects.all()
        serializer = EventsTitleWiseSerializer(user, many=True)
        return Response(serializer.data)