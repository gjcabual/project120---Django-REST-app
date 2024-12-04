from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .encryption import encrypt, decrypt
from .models import Message

class SendMessageView(View):
    def post(self, request):
        message = request.POST.get('message', '')
        if message:
            encrypted_message = encrypt(message)
            # Here you can save the encrypted message to a database or file
            Message.objects.create(encrypted_message=encrypted_message)
            # For demonstration, we'll just return it
            return JsonResponse({'encrypted_message': encrypted_message})
        return JsonResponse({'error': 'No message provided'}, status=400)

# class ReceiveMessageView(View):
#     def post(self, request):
#         encrypted_message = request.POST.get('encrypted_message', '')
#         if encrypted_message:
#             decrypted_message = decrypt(encrypted_message)
#             return JsonResponse({'decrypted_message': decrypted_message})
#         return JsonResponse({'error': 'No encrypted message provided'}, status=400)
    
class ReceiveMessageView(View):
    def get(self, request):
        # Fetch the latest encrypted message from the database
        latest_message = Message.objects.last()
        return render(request, 'receive.html', {'latest_message': latest_message})

    def post(self, request):
        encrypted_message = request.POST.get('encrypted_message', '')
        if encrypted_message:
            decrypted_message = decrypt(encrypted_message)
            return JsonResponse({'decrypted_message': decrypted_message})
        return JsonResponse({'error': 'No encrypted message provided'}, status=400)
    
class MessageFormView(View):
    def get(self, request):
        return render(request, 'message_form.html')
    
class ReceiveMessageFormView(View):
    def get(self, request):
        return render(request, 'receive.html')