
from django.urls import path

from accounts.views import TrainerCreateView,StudentCreateView

urlpatterns = [

    # trainer creation
    path("trainer/",TrainerCreateView.as_view()),

    # student creation
    path("student/",StudentCreateView.as_view()),
]