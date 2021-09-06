# imports
try:
    import os
    from .base import *

except Exception as e:
    print(e)

# DEBUG MODE
# It traverse developement two times?? but on updated one time traverse
DEBUG = os.environ['DEBUG']
print("Debug Mode:", DEBUG)

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [

    # developement specific
    'debug_toolbar'
]

# Debug Toolbar settings
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

# Debug MiddleWare
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

SHOW_TOOLBAR = os.environ['SHOW_TOOLBAR']
def show_toolbar(request):
    return SHOW_TOOLBAR

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar
}

# Local Mongo DB(NOSQL)
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'agora_database',
    }
}