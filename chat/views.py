from django.shortcuts import render
from chat.models import CheckUser
import time
from asgiref.sync import async_to_sync,sync_to_async
# Create your views here.

def lobby(request):
    users = CheckUser.objects.filter()
    user_list = []
    for user in users:
        if user.user != request.user:
            user_json = {
                "username": user.user.username,
                "status": "Online" if user.is_online
                 else "Offline"
            }

            user_list.append(user_json)
    return render(request, 'chat/lobby.html', context={"user_list":user_list})