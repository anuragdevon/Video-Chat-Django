from os import name
from django.urls import path
from .views import(
    index, 
    pusher_auth, 
    generate_agora_token,
    call_user
) 

# routing
urlpatterns = [
    path('', index, name='index'),
    path('pusher/auth/', pusher_auth, name='pusher-auth'),
    path('token/', generate_agora_token, name='agora-token'),
    path('call-user/',call_user, name='call-user')
]