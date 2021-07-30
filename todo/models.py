from django.db import models
from django.urls import reverse
from django.utils import timezone


class CategoryManger(models.Manager):
    def with_counts(self):
        return self.annotate(num_task=models.Count("task")).filter(num_task=0)


class Category(models.Model):
    name = models.CharField(max_length=30, default='None', unique=True)
    objects = models.Manager()  # The default manager
    tasks = CategoryManger()  # Our custom manager

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[str(self.id)])

    def list_ctg_tasks(self):
        list_task = self.task_set.all()
        if len(list_task) == 0:
            pass
        else:
            return list_task

    @staticmethod
    def list_ctg_no_tasks():
        list_no_task = Category.tasks.with_counts()
        return list_no_task

    def num_task_ctg(self):
        return self.task_set.all().count()


class ExpireTaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(expired__lte=timezone.now())


class Task(models.Model):
    class Meta:
        ordering = ('expired',)

    PRIORITY_TASK = [
        (0, 'بی اهمیت'),
        (1, 'کم اهمیت'),
        (2, 'توجه'),
        (3, 'قابل توجه'),
        (4, 'مهم'),
        (5, 'ضروری'),
    ]
    title = models.CharField('title', max_length=30)
    description = models.TextField(max_length=500)
    category = models.ManyToManyField(Category)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority = models.IntegerField(choices=PRIORITY_TASK, default=0)
    expired = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()  # The default manager
    expire_task = ExpireTaskManager()  # Our custom manager

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])

    @staticmethod
    def due_task():
        return Task.expire_task.get_queryset()

    def set_category(self):
        return self.category.all()