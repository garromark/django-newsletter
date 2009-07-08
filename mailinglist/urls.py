from django.conf.urls.defaults import *

urlpatterns = patterns('mailinglist.views',
    url(r'^$', 'newsletter_list', name='mailinglist_newsletter_list'),
    
    url(r'^(?P<newsletter_slug>[-\w]+)/$','newsletter_detail', name='mailinglist_newsletter_detail'),
    
    url(r'^(?P<newsletter_slug>[-\w]+)/subscribe/$', 'subscribe_request', name='mailinglist_newsletter_subscribe_request'),
    url(r'^(?P<newsletter_slug>[-\w]+)/update/$', 'update_request', name='mailinglist_newsletter_update_request'),
    url(r'^(?P<newsletter_slug>[-\w]+)/unsubscribe/$', 'unsubscribe_request', name='mailinglist_newsletter_unsubscribe_request'),
        
    url(r'^(?P<newsletter_slug>[-\w]+)/subscription/(?P<email>[-_a-zA-Z@\.]+)/(?P<action>[a-z]+)/activate/(?P<activation_code>[a-zA-Z0-9]+)/$', 'update_subscription', name='mailinglist_newsletter_update_activate'),
    url(r'^(?P<newsletter_slug>[-\w]+)/subscription/(?P<email>[-_a-zA-Z@\.]+)/(?P<action>[a-z]+)/activate/$', 'update_subscription', name='mailinglist_newsletter_update'),
    
    url(r'^(?P<newsletter_slug>[-\w]+)/archive/$','archive', name='mailinglist_newsletter_archive'),
)

