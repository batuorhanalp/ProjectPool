from django.conf.urls import patterns, include, url
from views import (
    IdeaList
)


urlpatterns = patterns('pool.views',
    url(r'^list/$', IdeaList.as_view()),
)
