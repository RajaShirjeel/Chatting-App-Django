from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Chat
from user.models import CustomUser
# Create your views here.
def all_chats(request):
    if not request.user.is_authenticated:
        return redirect('user:login_user')

    users = CustomUser.objects.all()
    return render(request, 'interaction/chats.html', {'users':users})

def chat_view(request, pk):
    other_user = CustomUser.objects.get(pk=pk)
    messages = Chat.objects.filter(
        Q(sender=request.user, receiver=other_user) | Q(sender=other_user, receiver=request.user)).all()
    return render(request, 'interaction/chat.html', {'user': other_user, 'messages':messages})

def create_message(request):
    other_user_pk = request.POST.get('other_user')
    other_user = CustomUser.objects.get(pk=other_user_pk)
    message = request.POST.get('message')
    Chat.objects.create(
        sender = request.user,
        receiver = other_user,
        message = message
    )
    return redirect('interaction:chat_page', pk=other_user.pk)