from django.shortcuts import render

# Create your views here.

def index(request):
    """create a view to render the home page"""
    return render(request, 'chat/index.html')


def room(request, room_name):
    """create a view to render a single chatroom"""
    return render(request, 'chat/chatroom.html', {'room_name' : room_name})