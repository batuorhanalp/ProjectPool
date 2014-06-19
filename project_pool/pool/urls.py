from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from views import *


from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def staff_member_required(view_func, redirect_field_name=REDIRECT_FIELD_NAME, login_url='admin:login'):
    """
    Decorator for views that checks that the user is logged in and is a staff
    member, displaying the login page if necessary.
    """
    return user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url='/giris-yap/',
        redirect_field_name=redirect_field_name
    )(view_func)


urlpatterns = patterns('pool.views',
    url(r'^/?$', login_required(UserDashboard.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="user_dashboard"),

    # Users
    url(r'^kullanici-yarat/?$', staff_member_required(UserCreation.as_view()), name="user_creation"),
    url(r'^kullanicilar/?$', staff_member_required(UserList.as_view()), name="user_list"),
    url(r'^kullanici-sil/?$', "user_multiple_deletion", name="cms_user_multiple_delete"),
    url(r'^kullanici-sil/(?P<pk>[a-zA-Z0-9]+)/$', staff_member_required(CMSUserDeletion.as_view()), name='cms_user_delete'),
    #url(r'^kullanici-guncelle/(?P<pk>[a-zA-Z0-9]+)/$', staff_member_required(CMSUserUpdation.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name='cms_user_updation'),

    # User ideas
    url(r'^fikirler/?$', login_required(UserIdeaList.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="user_idea_list"),

    # Idea
    url(r'^cms/fikirler/?$', login_required(CMSIdeaList.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_idea_list"),
    url(r'^cms/yeni-fikir/?$', login_required(CMSIdeaCreation.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_idea_creation"),
    #url(r'^cms/fikir/(?P<pk>[a-zA-Z0-9]+)/$', staff_member_required(IdeaDetail.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name='cms_idea_details'),
    url(r'^cms/fikir-guncelle/(?P<pk>[a-zA-Z0-9]+)/$', login_required(CMSIdeaUpdation.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name='cms_idea_updation'),
    url(r'^cms/fikir-sil/(?P<pk>[a-zA-Z0-9]+)/$', staff_member_required(CMSIdeaDeletion.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name='cms_idea_deletion'),
    url(r'^cms/fikir-sil/?$', "idea_multiple_deletion", name="cms_idea_multiple_delete"),

    # Brand
    url(r'^cms/markalar/?$', staff_member_required(CMSBrandList.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_brand_list"),
    url(r'^cms/yeni-marka/?$', staff_member_required(CMSBrandCreation.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_brand_creation"),
    url(r'^cms/marka-sil/?$', "brand_multiple_deletion", name="cms_brand_multiple_delete"),
    url(r'^cms/marka-sil/(?P<pk>[a-zA-Z0-9]+)/$', staff_member_required(CMSBrandDeletion.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name='cms_brand_delete'),
    url(r'^cms/marka-guncelle/(?P<pk>[a-zA-Z0-9]+)/$', staff_member_required(CMSBrandUpdation.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name='cms_brand_updation'),

    # Budget
    url(r'^cms/butceler/?$', staff_member_required(CMSBudgetList.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_budget_list"),
    url(r'^cms/yeni-butce/?$', staff_member_required(CMSBudgetCreation.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_budget_creation"),
    url(r'^cms/butce-sil/?$', "budget_multiple_deletion", name="cms_budget_multiple_delete"),
    url(r'^cms/butce-sil/(?P<pk>[a-zA-Z0-9]+)/$', staff_member_required(CMSBudgetDeletion.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name='cms_budget_delete'),
    url(r'^cms/butce-guncelle/(?P<pk>[a-zA-Z0-9]+)/$', staff_member_required(CMSBrandUpdation.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name='cms_budget_updation'),

    # Categories
    url(r'^cms/kategoriler/?$', staff_member_required(CMSCategoryList.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_category_list"),
    url(r'^cms/yeni-kategori/?$', staff_member_required(CMSCategoryCreation.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name="cms_category_creation"),
    url(r'^cms/kategori-sil/?$', "category_multiple_deletion", name="cms_category_multiple_delete"),
    url(r'^cms/kategori-sil/(?P<pk>[a-zA-Z0-9]+)/$', staff_member_required(CMSCategoryDeletion.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name='cms_category_delete'),
    url(r'^cms/kategori-guncelle/(?P<pk>[a-zA-Z0-9]+)/$', staff_member_required(CMSCategoryUpdation.as_view(), redirect_field_name=settings.REDIRECT_FIELD_NAME), name='cms_category_updation'),

    # search
    url(r'^search/?$', "search", name="search"),

    # settings
    url(r'^settings/?$', "settings_view", name="settings"),

    # undo
    url(r'^undo/?$', "undo_last_request", name="undo"),
    url(r'^undo-creation/?$', "undo_and_delete_last_request", name="undo_and_delete"),
)
