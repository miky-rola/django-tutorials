from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=False, blank=False)
    time_to_perform = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
    

