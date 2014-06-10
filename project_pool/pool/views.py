from django.views.generic import ListView, DetailView, CreateView, UpdateView
from models import (
    Brand,
    Idea,
    Budget,
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
    template_name = 'pool/cms/idea_list.html'

    def get_context_data(self, **kwargs):
        context = super(CMSIdeaList, self).get_context_data(**kwargs)
        context['in_cms'] = True
        return context


class CMSIdeaCreation(CreateView):
    u"""
    CMS/11-Karbonat Intranet - CMS_0003_Page 1 - Idea Panel
    """
    model = Idea
    fields = ['name', 'summary', 'detail', 'offerred_brands', 'dealt_brands',
              'categories', 'budget']
    template_name = 'pool/cms/idea_creation.html'


class CMSBrandList(ListView):
    u"""
    CMS/12-Karbonat Intranet - CMS_0001_Page 2 - Clients
    """
    model = Brand
    context_object_name = 'brands'
    paginate_by = 2
    template_name = 'pool/cms/brand_list.html'


class CMSBrandCreation(CreateView):
    u"""
    CMS/13-Karbonat Intranet - CMS_0004_Page 2 - Client Panel
    """
    model = Brand
    fields = ['name']
    template_name = 'pool/cms/brand_creation.html'


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


class CMSBudgetCreation(CreateView):
    model = Budget
    fields = ['start', 'end']
    template_name = 'pool/cms/budget_creation.html'


class CMSBudgetList(ListView):
    model = Budget
    context_object_name = 'budgets'
    paginate_by = 2
    template_name = 'pool/cms/budget_list.html'
