from django.db import models

# Create your models here.
# myapp/models.py

from django.db import models

class Message(models.Model):
    encrypted_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.encrypted_message