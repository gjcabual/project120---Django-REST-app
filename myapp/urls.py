# # myapp/urls.py

# from django.urls import path
# from .views import SendMessageView, ReceiveMessageView, MessageFormView


# urlpatterns = [
#     path('send/', SendMessageView.as_view(), name='send_message'),
#     path('receive/', ReceiveMessageView.as_view(), name='receive_message'),
#     path('message-form/', MessageFormView.as_view(), name='message_form'),
# ]

# myapp/urls.py

from django.urls import path
from .views import SendMessageView, ReceiveMessageView, MessageFormView

urlpatterns = [
    path('api/send/', SendMessageView.as_view(), name='send_message'),        # Updated to API endpoint
    path('api/receive/', ReceiveMessageView.as_view(), name='receive_message'),  # Updated to API endpoint
    path('', MessageFormView.as_view(), name='message_form'),  
]

