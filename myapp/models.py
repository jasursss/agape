from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# models.py

class BibleVerse(models.Model):
    reference = models.CharField(max_length=100)
    verse_text = models.TextField()
    date = models.DateField(default=timezone.now)
    reflection = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.reference} - {self.date}"

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return self.title
    
##################

class SharedVerse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verse = models.TextField()
    shared_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Verse shared by {self.user.username} at {self.shared_at}"