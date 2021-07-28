from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskDetailView,
    TaskUpdateView,
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    TaskView,
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('newtask/', TaskCreateView.as_view(), name='task_new'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task_update'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('newcategory/', CategoryCreateView.as_view(), name='category_new'),
    path('<int:pk>', CategoryDetailView.as_view(), name='category_detail'),
    path('task', TaskView.as_view(), name='task'),
]
