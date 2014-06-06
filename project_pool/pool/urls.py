from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from views import *


urlpatterns = patterns('pool.views',
    url(r'^/?$', login_required(UserDashboard.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="user_dashboard"),

    # Idea
    url(r'^cms/fikirler/?$', login_required(CMSIdeaList.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_idea_list"),
    url(r'^cms/yeni-fikir/?$', login_required(CMSIdeaCreation.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_idea_creation"),
    url(r'^cms/fikir/(?P<pk>[a-zA-Z0-9]+)/$', login_required(IdeaDetail.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name='cms_idea_details'),

    # Brand
    url(r'^cms/markalar/?$', login_required(CMSBrandList.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_brand_list"),
    url(r'^cms/yeni-marka/?$', login_required(CMSBrandCreation.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_brand_creation"),
)
