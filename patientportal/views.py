from django.contrib.auth.decorators import login_required
import os
import time
from django.contrib.auth.models import User
import json
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .agora_key.RtcTokenBuilder import RtcTokenBuilder, Role_Attendee
from pusher import Pusher



from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import PatientRegisterForm


from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}, please log in.')
            return redirect('login')
    else:
        form = PatientRegisterForm()
    return render(request, 'patientportal/register.html', {'form': form})


@login_required
def patientportalhome(request):
    User = get_user_model()
    all_users = User.objects.filter(is_superuser=True).exclude(id=request.user.id).only('id', 'username')
    return render(request, 'patientportal/patientportalhome.html',{'allUsers': all_users})


@login_required
def patientprofile(request):
    return render(request, 'patientportal/patientprofile.html')

# Instantiate a Pusher Client
pusher_client = Pusher(app_id=os.environ.get('PUSHER_APP_ID'),
                       key=os.environ.get('PUSHER_KEY'),
                       secret=os.environ.get('PUSHER_SECRET'),
                       ssl=True,
                       cluster=os.environ.get('PUSHER_CLUSTER')
                       )



def pusher_auth(request):
    payload = pusher_client.authenticate(
        channel=request.POST['channel_name'],
        socket_id=request.POST['socket_id'],
        custom_data={
            'user_id': request.user.id,
            'user_info': {
                'id': request.user.id,
                'name': request.user.username
            }
        })
    return JsonResponse(payload)


def generate_agora_token(request):
    appID = os.environ.get('AGORA_APP_ID')
    appCertificate = os.environ.get('AGORA_APP_CERTIFICATE')
    channelName = json.loads(request.body.decode(
        'utf-8'))['channelName']
    userAccount = request.user.username
    expireTimeInSeconds = 3600
    currentTimestamp = int(time.time())
    privilegeExpiredTs = currentTimestamp + expireTimeInSeconds

    token = RtcTokenBuilder.buildTokenWithAccount(
        appID, appCertificate, channelName, userAccount, Role_Attendee, privilegeExpiredTs)

    return JsonResponse({'token': token, 'appID': appID})


def call_user(request):
    body = json.loads(request.body.decode('utf-8'))

    user_to_call = body['user_to_call']
    channel_name = body['channel_name']
    caller = request.user.id

    pusher_client.trigger(
        'presence-online-channel',
        'make-agora-call',
        {
            'userToCall': user_to_call,
            'channelName': channel_name,
            'from': caller
        }
    )
    return JsonResponse({'message': 'call has been placed'})
