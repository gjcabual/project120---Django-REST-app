# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views import View
# from .encryption import encrypt, decrypt
# from .models import Message

# class SendMessageView(View):
#     def post(self, request):
#         message = request.POST.get('message', '')
#         if message:
#             encrypted_message = encrypt(message)
#             # Here you can save the encrypted message to a database or file
#             Message.objects.create(encrypted_message=encrypted_message)
#             # For demonstration, we'll just return it
#             return JsonResponse({'encrypted_message': encrypted_message})
#         return JsonResponse({'error': 'No message provided'}, status=400)

# class ReceiveMessageView(View):
#     def get(self, request):
#         # Fetch the latest encrypted message from the database
#         latest_message = Message.objects.last()
#         return render(request, 'receive.html', {'latest_message': latest_message})

#     def post(self, request):
#         encrypted_message = request.POST.get('encrypted_message', '')
#         if encrypted_message:
#             decrypted_message = decrypt(encrypted_message)
#             return JsonResponse({'decrypted_message': decrypted_message})
#         return JsonResponse({'error': 'No encrypted message provided'}, status=400)
    
# class MessageFormView(View):
#     def get(self, request):
#         return render(request, 'message_form.html')
    
# class ReceiveMessageFormView(View):
#     def get(self, request):
#         return render(request, 'receive.html')


# myapp/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .encryption import encrypt, decrypt
from .models import Message
from .serializers import MessageSerializer
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

class SendMessageView(APIView):
    def post(self, request):
        message = request.data.get('message', '')
        sender_name = request.data.get('sender_name', '')  # Capture sender_name
        if message and sender_name:
            encrypted_message = encrypt(message)
            Message.objects.create(encrypted_message=encrypted_message, sender_name=sender_name)
            return Response({'encrypted_message': encrypted_message}, status=status.HTTP_201_CREATED)
        return Response({'error': 'No message provided'}, status=status.HTTP_400_BAD_REQUEST)

# class ReceiveMessageView(APIView):
#     def get(self, request):
#         latest_message = Message.objects.last()
#         if latest_message:
#             serializer = MessageSerializer(latest_message)
#             return Response(serializer.data)
#         return Response({'error': 'No messages found'}, status=status.HTTP_404_NOT_FOUND)

class ReceiveMessageView(APIView):
    def get(self, request):
        latest_message = Message.objects.last()
        sender_name = request.data.get('sender_name', '')  # Get sender_name
        if latest_message:
            decrypted_message = decrypt(latest_message.encrypted_message)
            return Response({
                'id': latest_message.id,
                'sender_name': latest_message.sender_name,
                'encrypted_message': latest_message.encrypted_message,
                'decrypted_message': decrypted_message
            })
        return Response({'error': 'No messages found'}, status=status.HTTP_404_NOT_FOUND)




class MessageFormView(View):
    def get(self, request):
        return render(request, 'message_form.html')  # Render your HTML template

class ReceiveMessageFormView(View):
    def get(self, request):
        latest_message = Message.objects.last()
        decrypted_message = None
        if latest_message:
            decrypted_message = decrypt(latest_message.encrypted_message)
        return render(request, 'receive.html', {
            'latest_message': latest_message,
            'decrypted_message': decrypted_message
        })
        

    def post(self, request):
        encrypted_message = request.POST.get('encrypted_message', '')
        if encrypted_message:
            decrypted_message = decrypt(encrypted_message)
            return JsonResponse({'encrypted_message': encrypted_message,'decrypted_message': decrypted_message})
        return JsonResponse({'error': 'No encrypted message provided'}, status=400)
    
# Registration and Login
class RegisterView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        response = requests.post(
            'https://<your-nhost-project>.nhost.app/v1/signup',
            json={'email': email, 'password': password}
        )

        return JsonResponse(response.json(), status=response.status_code)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        response = requests.post(
            'https://<your-nhost-project>.nhost.app/v1/login',
            json={'email': email, 'password': password}
        )

        if response.status_code == 200:
            # Store user session or token as needed
            return JsonResponse(response.json(), status=response.status_code)
        return JsonResponse(response.json(), status=response.status_code)
    

    