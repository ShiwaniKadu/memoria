from django.db import models
from django.utils import timezone

class JournalType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type
class Journal(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length = 50)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=100)
    journal_type = models.ForeignKey(JournalType, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

