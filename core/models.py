from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, blank=True)  # Beginner, Intermediate, Advanced
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name