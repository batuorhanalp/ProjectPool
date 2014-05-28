from django.conf.urls import patterns, include, url
from views import (
    IdeaList,
    IdeaDetail,
)


urlpatterns = patterns('pool.views',
    url(r'^list/$', IdeaList.as_view(), name="idea-list"),
    url(r'^list/(?P<pk>\d+)/$', IdeaDetail.as_view(), name='idea-detail'),
)
