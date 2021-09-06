try:
    import os
    from .base import *

except Exception as e:
    print(e)

# DEBUG MODE
DEBUG = os.environ['DEBUG']
print("Debug Mode:", DEBUG)

ALLOWED_HOSTS = ['ip-address', 'https://zyz.com/']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'agora_database',
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': ''
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.psycopg2',
#         'NAME': os.environ['DB_NAME'],
#         'USER': os.environ['DB_USER'],
#         'PASSWORD': os.environ['DB_PASSWORD'],
#         'HOST': os.environ['DB_HOST'],
#         'PORT': ''
#     }
# }