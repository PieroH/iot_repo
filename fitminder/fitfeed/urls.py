from django.urls import path
from . import views
from .views import EventListView, EventCreateView, EventDetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('events/new/', EventCreateView.as_view(), name='event-form'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    # path('<int:year>/<str:month>/', views.home, name='home'),
    path('feed/', views.feed, name='feed'),
]