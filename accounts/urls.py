
from django.urls import path

from accounts.views import TrainerCreateView,StudentCreateView
from accounts.views import TrainerProfileUpdateView,TrainerprofileGetView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [

    # trainer creation
    path("trainer/",TrainerCreateView.as_view()),

    # student creation
    path("student/",StudentCreateView.as_view()),

    #token creation
    path("token/",ObtainAuthToken.as_view()),

    #trainer profile updation
    path("trainer/profile/complete/",TrainerProfileUpdateView.as_view()),

    #trainer profile detailing
    path("trainer/profile/me/",TrainerprofileGetView.as_view()),

  
]
