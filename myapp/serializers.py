# myapp/serializers.py

from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'encrypted_message','sender_name', 'created_at']  # Specify fields you want to expose