from django.db import models

# Create your models here.
# myapp/models.py

from django.db import models

class Message(models.Model):
    encrypted_message = models.TextField()
    sender_name = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender_name}: {self.encrypted_message}"