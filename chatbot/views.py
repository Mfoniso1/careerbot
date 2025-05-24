from django.shortcuts import render
from django.http import JsonResponse

def chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        reply = f"You asked: '{message}', but I’m not smart yet!"
        return JsonResponse({'reply': reply})
    
    return render(request, 'chatbot/chat.html')
