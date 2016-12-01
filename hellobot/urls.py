from django.conf.urls import patterns, include, url
from django.contrib import admin
import chatbot.views as v

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hellobot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$' , v.index),
    #url(r'', 'chatbot.views.index'),
    url(r'^facebook_auth/?$' , v.MyChatBotView.as_view()) ,
    url(r'^resume2/(?P<id>[\*\w\-]+)$' ,v.resume_2 , name = 'event') , 
    url(r'^resume1/(?P<id>[\*\w\-]+)$' ,v.resume_1 , name = 'event2'),
    url(r'^temp2/(?P<id>[\*\w\-]+)$' ,v.eventweb2 , name = 'event2'),
    url(r'^blah/?$' ,v.index , name = 'index') ,
    
)
