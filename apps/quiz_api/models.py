from django.db import models
import datetime
from django_mysql.models import JSONField, Model

class Category(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Category object: {self.title} ({self.id})>"

class Quiz(models.Model):
    title = models.CharField(max_length=40)
    # difficulty = models.IntegerField()
    description = models.TextField(default="")
    timed = models.BooleanField(default="False")
    category = models.ForeignKey(Category, related_name="quizes", blank=True, null=True, on_delete=models.CASCADE)
    # questions = models.ManyToManyField(Question, blank=True, null=True, related_name="quizes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Quiz object: {self.title} ({self.id})>"


class Question(models.Model):
    content = JSONField()
    category = models.ForeignKey(Category, related_name="questions", on_delete=models.CASCADE)
    multiple = models.BooleanField(default=False)
    quiz = models.ForeignKey(Quiz, related_name="questions", blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Question object: {self.content} ({self.id})>"

