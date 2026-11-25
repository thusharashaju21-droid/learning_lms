
from django.urls import path

from units.views import ModuleCreateView,ModuleRetreiveUpdateDeleteView

urlpatterns = [

    #module create view
    path("course/<int:pk>/modules/",ModuleCreateView.as_view()),

    #module retrieve,update,delete view
    path("module/<int:pk>/",ModuleRetreiveUpdateDeleteView.as_view()),
]