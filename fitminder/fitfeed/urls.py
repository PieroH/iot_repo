from django.urls import path
from . import views
from fitfeed.views import OneOffReminderView, ReminderCreateView, ReminderEditView, ReminderListView, DeleteReminderView

urlpatterns = [
    path('', ReminderListView.as_view(), name='index'),
    path('reminder/new/', ReminderCreateView.as_view(), name='reminder-create'),
    path('reminder/<int:pk>/', ReminderEditView.as_view(), name='reminder-edit'),
    path('reminder/oneoff/', OneOffReminderView.as_view(), name='reminder-oneoff'),
    path('reminder/<int:pk>/delete/', DeleteReminderView.as_view(), name='reminder-delete')
]