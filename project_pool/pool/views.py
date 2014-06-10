from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView,
)
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from models import (
    Brand,
    Idea,
    Budget,
    Category,
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
    template_name = 'pool/cms/idea_list.html'


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


class CMSBrandDeletion(DeleteView):
    model = Brand
    success_url = reverse_lazy('pool:cms_brand_list')
    template_name = 'pool/cms/brand_delete.html'


@login_required
@require_http_methods(["POST"])
def brand_multiple_deletion(request):
    """
    delete multiple brands at once.
    get brand_id array as request param
    """
    # TODO: get ile emin misiniz ekrani yap, post ile sil
    # if request.method == "POST":

    brand_ids = request.POST.getlist('brand_id[]')
    brands = Brand.objects.filter(id__in=brand_ids)
    for brand in brands:
        brand.delete()
    return redirect("pool:cms_brand_list")


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


class CMSBudgetDeletion(DeleteView):
    model = Budget
    success_url = reverse_lazy('pool:cmd_budget_list')
    template_name = 'pool/cms/budget_delete.html'


@login_required
@require_http_methods(["POST"])
def budget_multiple_deletion(request):
    """
    delete multiple budgets at once.
    get budget_id array as request param
    """
    # TODO: get ile emin misiniz ekrani yap, post ile sil
    # if request.method == "POST":

    budget_ids = request.POST.getlist('budget_id[]')
    budgets = Budget.objects.filter(id__in=budget_ids)
    for budget in budgets:
        budget.delete()
    return redirect("pool:cms_budget_list")


class CMSCategoryCreation(CreateView):
    model = Category
    fields = ['name']
    template_name = 'pool/cms/category_creation.html'


class CMSCategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    paginate_by = 2
    template_name = 'pool/cms/category_list.html'


class CMSCategoryDeletion(DeleteView):
    model = Category
    success_url = reverse_lazy('pool:cms_category_list')
    template_name = 'pool/cms/category_delete.html'


@login_required
@require_http_methods(["POST"])
def category_multiple_deletion(request):
    """
    delete multiple categories at once.
    get category_id array as request param
    """
    # TODO: get ile emin misiniz ekrani yap, post ile sil
    # if request.method == "POST":

    category_ids = request.POST.getlist('category_id[]')
    categories = Category.objects.filter(id__in=category_ids)
    for category in categories:
        category.delete()
    return redirect("pool:cms_category_list")
