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
    url(r'^cms/marka-sil/?$', "brand_multiple_deletion", name="cms_brand_multiple_delete"),
    url(r'^cms/marka-sil/(?P<pk>[a-zA-Z0-9]+)/$', login_required(CMSBrandDeletion.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name='cms_brand_delete'),

    # Budget
    url(r'^cms/butceler/?$', login_required(CMSBudgetList.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_budget_list"),
    url(r'^cms/yeni-butce/?$', login_required(CMSBudgetCreation.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_budget_creation"),
    url(r'^cms/butce-sil/?$', "budget_multiple_deletion", name="cms_budget_multiple_delete"),
    url(r'^cms/butce-sil/(?P<pk>[a-zA-Z0-9]+)/$', login_required(CMSBudgetDeletion.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name='cms_budget_delete'),

    # Categories
    url(r'^cms/kategoriler/?$', login_required(CMSCategoryList.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_category_list"),
    url(r'^cms/yeni-kategori/?$', login_required(CMSCategoryCreation.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_category_creation"),
    url(r'^cms/kategori-sil/?$', "category_multiple_deletion", name="cms_category_multiple_delete"),
    url(r'^cms/kategori-sil/(?P<pk>[a-zA-Z0-9]+)/$', login_required(CMSCategoryDeletion.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name='cms_category_delete'),

    # search
    url(r'^search/?$', "search", name="search"),
)
