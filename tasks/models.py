from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

# Create your models here.
class Task(models.Model):
    project = models.ForeignKey("project", on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=255)
    description= models.TextField()
    assign_to = models.ManyToManyField(Employee)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
class TaskDetails(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH, 'High'),
        (MEDIUM,'Medium'),
        (LOW,'Low')
    )
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    assign_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default=LOW)
    
    
class Project(models.Model):
    name = models.CharField(max_length=250)
    start_date = models.DateField()