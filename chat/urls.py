from django.conf.urls import patterns, url


urlpatterns = patterns('chat.views',
    url(r'^$', 'index'),
    url(r'^submit/', 'submit_message'),
)
