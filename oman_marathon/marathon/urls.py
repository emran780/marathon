from django.urls import path
from .views import welcome, about, login, user_actions, past_events

urlpatterns = [
    path('', welcome, name='welcome'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('user-actions/', user_actions, name='user_actions'),
    path('past-events/', past_events, name='past_events'),
    
]


