from django.urls import path
from .views import  UploadView, SignUpApi,ResetPassword,NewPassword,UpdateAccount,AdminPanel,ChangePasswordView,GetAllUserView
from rest_framework.authtoken import views

user_list = GetAllUserView.as_view({                #for MoedlViewset we have to give http methods for url
    'get': 'list'
})

urlpatterns = [
    path('signup/', SignUpApi.as_view(),name="signup"),
    path('login/',views.obtain_auth_token),
    path('update/<str:pk>',UpdateAccount.as_view(), name="update"),
    path("forget-password/",ResetPassword.as_view()),
    path("reset-password/",NewPassword.as_view()),
    path('upload/<str:pk>', UploadView.as_view(), name='file-upload'),
    path('change-password/<int:pk>',ChangePasswordView.as_view(),name='change-password'),
    path('getalluser/',user_list,name='allusers')

]  