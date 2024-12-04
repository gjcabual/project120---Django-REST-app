# myapp/urls.py

from django.urls import path
from .views import SendMessageView, ReceiveMessageView, MessageFormView


urlpatterns = [
    path('send/', SendMessageView.as_view(), name='send_message'),
    path('receive/', ReceiveMessageView.as_view(), name='receive_message'),
    path('message-form/', MessageFormView.as_view(), name='message_form'),
]

