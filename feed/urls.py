from django.urls import path
from . import views
from .views import TweetListView,TweetCreateView,TweetUpdateView


urlpatterns = [
    path('', TweetListView.as_view(),name = 'home'),
    path('create/', TweetCreateView.as_view(),name = 'tweetcreate'),
    path('tweet/<int:pk>/update', TweetUpdateView.as_view(),name = 'tweetupdate')
]
