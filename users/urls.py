from django.urls import path
from . import views

urlpatterns = [
    path('getall/', views.UserListView.as_view(), name='user-list'),
    path('create/', views.UserCreateView.as_view()),
    path('add/', views.add, name='user-add'),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>', views.UserDeleteView.as_view(), name='user-delete'),
]
