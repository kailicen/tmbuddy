from django.urls import path
from . import views
from .views import (
    SelfReflectionCreateView, BuddyFeedbackCreateView, 
    SelfReflectionListView, GivenFeedbackListView, ReceivedFeedbackListView,
    SelfReflectionUpdateView, BuddyFeedbackUpdateView, 
    SelfReflectionDeleteView, BuddyFeedbackDeleteView, 
)


urlpatterns = [
    path('', views.home, name='tmbuddy-home'),
    path('reflection/new/', SelfReflectionCreateView.as_view(), name='reflection-create'),
    path('feedback/new/', BuddyFeedbackCreateView.as_view(), name='feedback-create'),
    path('reflection/<str:username>/', SelfReflectionListView.as_view(), name='user-reflection'),
    path('given-feedback/<str:username>/', GivenFeedbackListView.as_view(), name='user-given-feedback'),
    path('received-feedback/<str:username>/', ReceivedFeedbackListView.as_view(), name='user-received-feedback'),
    path('reflection/<int:pk>/update/', SelfReflectionUpdateView.as_view(), name='reflection-update'),
    path('feedback/<int:pk>/update/', BuddyFeedbackUpdateView.as_view(), name='feedback-update'),
    path('reflection/<int:pk>/delete/', SelfReflectionDeleteView.as_view(), name='reflection-delete'),
    path('feedback/<int:pk>/delete/', BuddyFeedbackDeleteView.as_view(), name='feedback-delete'),
    path('about/', views.about, name='tmbuddy-about'),
    path('tm_fam/', views.tm_fam, name='tmbuddy-tm-fam'),
    path('resources/', views.resources, name='tmbuddy-resources'),
]