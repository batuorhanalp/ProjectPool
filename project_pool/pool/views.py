from django.views.generic import ListView, DetailView, CreateView, UpdateView
from models import (
    Idea
)


class IdeaDetail(DetailView):
    model = Idea
    template_name = 'pool/cms/idea_details.html'


###
# USER
###


class UserDashboard(ListView):
    u"""
    USER/01-Karbonat_Intranet_0000_Page 1 - Index
    """
    model = Idea
    context_object_name = 'ideas'
    paginate_by = 2
    template_name = 'pool/user_dashboard.html'


###
# CMS
###


class CMSIdeaList(UserDashboard):
    u"""
    CMS/10-Karbonat Intranet - CMS_0000_Page 1 - Idea
    """
    pass


class CMSIdeaCreation(CreateView):
    u"""
    CMS/11-Karbonat Intranet - CMS_0003_Page 1 - Idea Panel
    """
    model = Idea
    fields = ['name', 'summary', 'detail', 'offerred_brands', 'dealt_brands', 'categories', 'budget']
    template_name = 'pool/cms/idea_creation.html'


class CMSClientList(ListView):
    u"""
    CMS/12-Karbonat Intranet - CMS_0001_Page 2 - Clients
    """
    pass


class CMSClientCreation(CreateView):
    u"""
    CMS/13-Karbonat Intranet - CMS_0004_Page 2 - Client Panel
    """
    pass


class CMSUserList(ListView):
    u"""
    CMS/14-Karbonat Intranet - CMS_0002_Page 3 - User
    """
    pass


class CMSUserCreation(CreateView):
    u"""
    CMS/15-Karbonat Intranet - CMS_0005_Page 3 - User Panel
    """
    pass


class CMSSettings(UpdateView):
    u"""
    CMS/16-Karbonat Intranet - CMS_0006_Page 4 - General Settings
    """
    pass