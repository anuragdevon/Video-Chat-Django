from os import environ

from django.http import response


try:
    import os
    import time
    import json
    from dotenv import load_dotenv
    
    from django.http.response import JsonResponse
    from django.contrib.auth import get_user_model
    from django.contrib.auth.decorators import login_required
    from django.shortcuts import render

    from .agora_key.RtcTokenBuilder import RtcTokenBuilder, Role_Attendee
    from pusher import Pusher

except Exception as e:
    print("Import Error:", e)

else:
    # Load Environment Variables
    load_dotenv()

    # Instantiate a Pusher Client           ###(Realtime communication channel using websockets)
    pusher_client = Pusher (
        app_id = os.environ['PUSHER_ID'],
        key = os.environ['PUSHER_KEY'],
        secret = os.environ['PUSHER_SECRET'],
        ssl = True,
        cluster = os.environ['PUSHER_CLUSTER']
    )

    # admin login
    @login_required(login_url='/admin/')        ### how decorators work and login decorator
    def index(request):
        User = get_user_model()
        all_users = User.objects.exclude(id=request.user.id).only('id', 'username')   ###

        response = {
            'allusers': all_users
        }

        return render(request, 'agora/index.html', response)

    # Pusher Authentication                             ###
    def pusher(request):
        payload = pusher_client.authenticate(
            channel = request.POST['channel_name'],
            socket_id = request.POST['socket_id'],
            custom_data = {
                'user_id': request.user.id,
                'user_info': {
                    'name': request.user.username
                }
            }
        )
        # change pusher to json format ??
        return JsonResponse(payload)

    # Generate Agora token                                              ###
    def generate_agora_token(request):
        app_ID = os.environ['AGORA_APP_ID']
        app_certificate = os.environ['AGORA_APP_CERTIFICATE']
        channel_name = json.loads(request.body.decode('utf-8'))['channelName']
        user_account = request.user.username
        expire_time_seconds = 3600
        current_timestamp = int(time.time())
        priviledge_expired_ts = current_timestamp + expire_time_seconds

        token = RtcTokenBuilder.buildTokenWithAccount(
            app_ID, app_certificate, channel_name, user_account, Role_Attendee, priviledge_expired_ts
        )

        response = {
            'token': token,
            'app_ID': app_ID
        }

        return JsonResponse(response) 

    # Call user function
    def call_user(request):                             ###
        body = json.loads(request.body.decode('utf-8'))
        
        user_to_call = body['user_to_call']
        channel_name = body['channel_name']
        caller = request.user.id

        call_details = {
            'user_to_call': user_to_call,
            'channel_name': channel_name,
            'from': caller
        }

        pusher_client.trigger(
            'presence-online-channel',
            'make-agora-call',
            call_details,
        )

        response = {
            'message': 'call has been placed'
        }

        return JsonResponse(response)