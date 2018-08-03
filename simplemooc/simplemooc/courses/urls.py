from django.conf.urls import  include, url
from simplemooc.courses.views import courses

urlpatterns = [
    url(r'^$', courses, name='courses'),
    url(r'^(?P<pk>\d+)/', details, name='details'),
]
