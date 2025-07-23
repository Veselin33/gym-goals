from django.db import models
from django.conf import settings

class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='goals')
    description = models.TextField(blank=True)
    target_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    achieved = models.BooleanField(default=False)

    def __str__(self):
        return f" {'Achieved' if self.achieved else 'Pending'}"
