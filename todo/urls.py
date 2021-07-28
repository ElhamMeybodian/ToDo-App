from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    CategoryListView,
    CategoryDetailView,
    TaskView,
)

urlpatterns = [
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('new/', TaskCreateView.as_view(), name='task_new'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('', TaskListView.as_view(), name='task_list'),
    path('task', TaskView.as_view(), name='task'),
]
