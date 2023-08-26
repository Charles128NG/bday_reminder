from django.urls import path
from . import views

app_name = 'notifier'
urlpatterns = [
    #path('friend-list/', views.friend_list, name='friend_list'),
    path('bday_list/', views.b_day_list, name='b_day_list'),
]