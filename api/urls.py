from . import views
from django.urls import path,include

urlpatterns=[
    path('',views.RequestList.as_view(),name='index'),
    path('/ambulance',views.AmbulanceList.as_view(),name='index'),
]