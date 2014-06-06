from django.conf.urls import patterns, include, url
from views import (
    UserDashboard,
    CMSIdeaList,
    CMSIdeaCreation,
    IdeaDetail,
)


urlpatterns = patterns('pool.views',
    url(r'^/?$', UserDashboard.as_view(), name="user_dashboard"),
    url(r'^cms/fikirler/?$', CMSIdeaList.as_view(), name="cms_idea_list"),
    url(r'^cms/yeni-fikir/?$', CMSIdeaCreation.as_view(), name="cms_idea_creation"),
    url(r'^list/(?P<pk>[a-zA-Z0-9]+)/$', IdeaDetail.as_view(), name='cms_idea_details'),
)
