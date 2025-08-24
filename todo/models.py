from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta,datetime
from django.utils.text import slugify
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Todo(models.Model): 
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateTimeField(blank=True, null=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def mark_completed(self):
        self.status = 'completed'
        self.completed_at = timezone.now()  
        self.save()

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = timezone.now() + timedelta(days=7)
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Todo.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def title_change(self):
        if self.pk:
            old_title = Todo.objects.get(pk=self.pk).title
            return old_title != self.title
        return True
    
    def __str__(self):
        return f"{self.title} ({self.status})"