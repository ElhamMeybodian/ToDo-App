from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Task, Category
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializers


# Create your views here.
# task view
class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_new.html'
    fields = '__all__'


class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'task_update.html'


class TaskView(APIView):
    def get(self, request, *args, **kwargs):
        # serializer = [TaskSerializers(task).data for task in Task.objects.all()]
        serializer = TaskSerializers(Task.objects.all(), many=True)
        return Response({'task': serializer.data})


# category view
class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_new.html'
    fields = '__all__'
