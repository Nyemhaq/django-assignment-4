from django.db import models
from category.models import Category

class Task(models.Model):
    title = models.CharField(max_length = 100)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    is_completed = models.BooleanField(default = False)
    assign_date = models.DateField()
    
    def __str__(self):
            return self.title
