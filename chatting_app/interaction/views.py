from django.shortcuts import render, redirect

# Create your views here.
def chat_page(request):
    if not request.user.is_authenticated:
        return redirect('user:login_user')

    return render(request, 'interaction/chat.html')
