from django.shortcuts import render, redirect

# Create your views here.
def all_chats(request):
    if not request.user.is_authenticated:
        return redirect('user:login_user')

    return render(request, 'interaction/chats.html')

def chat_view(request):
    return render(request, 'interaction/chat.html')