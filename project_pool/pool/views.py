from datetime import datetime
from django.views.generic import (
    ListView, CreateView,
    UpdateView, DeleteView, FormView,
)
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from models import (
    Brand,
    Idea,
    Budget,
    Category,
)
from reversion.models import (
    Revision
)
from forms import (
    UserForm
)


###
# USER
###


class UserCreation(SuccessMessageMixin, FormView):
    template_name = 'pool/user_creation.html'
    form_class = UserForm
    success_url = '/'

    def form_valid(self, form):
        """save the form now"""
        if form.cleaned_data['permission'] == "user":
            # admin
            User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password1']
            )
        elif form.cleaned_data['permission'] == "admin":
            # user
            User.objects.create_superuser(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password1']
            )

        return super(UserCreation, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return '%s kullanicisi yaratildi. <a href="%s">geri al</a>' %\
            (cleaned_data['username'], reverse('pool:undo'))

# class CMSUserUpdation(CMSBrandBase, UpdateView):
#    def get_success_message(self, cleaned_data):
#        return '%s isimli marka guncellendi. <a href="%s">geri al</a>' %\
#            (cleaned_data['name'], reverse('pool:undo'))


class UserList(ListView):
    model = User
    context_object_name = 'users'
    paginate_by = 10
    template_name = 'pool/user_list.html'


class CMSUserDeletion(DeleteView):
    model = User
    success_url = reverse_lazy('pool:user_list')
    template_name = 'pool/cms/deletion.html'


@login_required
@staff_member_required
@require_http_methods(["POST"])
def user_multiple_deletion(request):
    """
    delete multiple users at once.
    get user_id array as request param
    """
    # TODO: get ile emin misiniz ekrani yap, post ile sil
    # if request.method == "POST":

    user_ids = request.POST.getlist('user_id[]')
    users = User.objects.filter(id__in=user_ids)
    for user in users:
        user.delete()
    return redirect("pool:user_list")


class UserDashboard(ListView):
    u"""
    USER/01-Karbonat_Intranet_0000_Page 1 - Index
    """
    model = Idea
    context_object_name = 'ideas'
    paginate_by = 10
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


class UserIdeaList(UserDashboard):
    u"""
    CMS/10-Karbonat Intranet - CMS_0000_Page 1 - Idea
    """
    template_name = 'pool/cms/idea_list.html'

    def get_context_data(self, **kwargs):
        context = super(UserIdeaList, self).get_context_data(**kwargs)
        context['in_cms'] = False
        return context


class CMSIdeaBase(SuccessMessageMixin):
    model = Idea
    fields = ['name', 'summary', 'detail', 'offerred_brands', 'dealt_brands',
              'categories', 'budget']
    template_name = 'pool/cms/idea_creation.html'

    def get_success_url(self):
        return reverse('pool:user_idea_list')


class CMSIdeaCreation(CMSIdeaBase, CreateView):
    u"""
    CMS/11-Karbonat Intranet - CMS_0003_Page 1 - Idea Panel
    """
    def get_success_message(self, cleaned_data):
        return '%s isimli fikir yaratildi. <a href="%s">geri al</a>' %\
            (cleaned_data['name'], reverse('pool:undo_and_delete'))


class CMSIdeaUpdation(CMSIdeaBase, UpdateView):
    def get_success_message(self, cleaned_data):
        return '%s isimli fikir guncellendi. <a href="%s">geri al</a>' %\
            (cleaned_data['name'], reverse('pool:undo'))


class CMSIdeaDeletion(DeleteView):
    model = Idea
    success_url = reverse_lazy('pool:cms_idea_list')
    template_name = 'pool/cms/deletion.html'


class CMSBrandList(ListView):
    u"""
    CMS/12-Karbonat Intranet - CMS_0001_Page 2 - Clients
    """
    model = Brand
    context_object_name = 'brands'
    paginate_by = 10
    template_name = 'pool/cms/brand_list.html'


class CMSBrandBase(SuccessMessageMixin):
    model = Brand
    fields = ['name']
    template_name = 'pool/cms/brand_creation.html'

    def get_success_url(self):
        return reverse('pool:cms_brand_list')


class CMSBrandCreation(CMSBrandBase, CreateView):
    u"""
    CMS/13-Karbonat Intranet - CMS_0004_Page 2 - Client Panel
    """
    def get_success_message(self, cleaned_data):
        return '%s isimli marka yaratildi. <a href="%s">geri al</a>' %\
            (cleaned_data['name'], reverse('pool:undo_and_delete'))


class CMSBrandUpdation(CMSBrandBase, UpdateView):
    u"""
    CMS/13-Karbonat Intranet - CMS_0004_Page 2 - Client Panel
    """
    def get_success_message(self, cleaned_data):
        return '%s isimli marka guncellendi. <a href="%s">geri al</a>' %\
            (cleaned_data['name'], reverse('pool:undo'))


class CMSBrandDeletion(DeleteView):
    model = Brand
    success_url = reverse_lazy('pool:cms_brand_list')
    template_name = 'pool/cms/deletion.html'


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


@login_required
@staff_member_required
def settings_view(request):
    budgets = Budget.objects.all()
    categories = Category.objects.all()
    context = {
        "budgets": budgets,
        "categories": categories,
    }
    return render_to_response("pool/cms/settings.html", context,
                              context_instance=RequestContext(request)
                              )



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


class CMSBudgetBase(SuccessMessageMixin):
    model = Budget
    fields = ['start', 'end']
    template_name = 'pool/cms/budget_creation.html'

    def get_success_url(self):
        return reverse('pool:settings')


class CMSBudgetCreation(CMSBudgetBase, CreateView):
    def get_success_message(self, cleaned_data):
        return '$%s - $%s isimli butce yaratildi. <a href="%s">geri al</a>' %\
            (cleaned_data['start'], cleaned_data['end'], reverse('pool:undo_and_delete'))


class CMSBudgetUpdation(CMSBudgetBase, UpdateView):
    def get_success_message(self, cleaned_data):
        return '$%s - $%s isimli butce guncellendi. <a href="%s">geri al</a>' %\
            (cleaned_data['start'], cleaned_data['end'], reverse('pool:undo'))


class CMSBudgetList(ListView):
    model = Budget
    context_object_name = 'budgets'
    paginate_by = 10
    template_name = 'pool/cms/budget_list.html'


class CMSBudgetDeletion(DeleteView):
    model = Budget
    success_url = reverse_lazy('pool:cmd_budget_list')
    template_name = 'pool/cms/budget_delete.html'


@login_required
@staff_member_required
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
    return redirect("pool:settings")


class CMSCategoryBase(SuccessMessageMixin):
    model = Category
    fields = ['name']
    template_name = 'pool/cms/category_creation.html'

    def get_success_url(self):
        return reverse('pool:settings')


class CMSCategoryCreation(CMSCategoryBase, CreateView):
    def get_success_message(self, cleaned_data):
        return '%s isimli kategori yaratildi. <a href="%s">geri al</a>' %\
            (cleaned_data['name'], reverse('pool:undo_and_delete'))


class CMSCategoryUpdation(CMSCategoryBase, UpdateView):
    def get_success_message(self, cleaned_data):
        return '%s isimli kategori guncellendi. <a href="%s">geri al</a>' %\
            (cleaned_data['name'], reverse('pool:undo'))


class CMSCategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    paginate_by = 10
    template_name = 'pool/cms/category_list.html'


class CMSCategoryDeletion(DeleteView):
    model = Category
    success_url = reverse_lazy('pool:cms_category_list')
    template_name = 'pool/cms/category_delete.html'


@login_required
@staff_member_required
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
    return redirect("pool:settings")


@login_required
@require_http_methods(["GET"])
def search(request):
    """searches the entire app"""

    # get variables
    offerred_brand_ids = request.GET.getlist('offerred_brands')
    dealt_brand_ids = request.GET.getlist('dealt_brands')
    category_ids = request.GET.getlist('categories')
    budget_ids = request.GET.getlist('budgets')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    q = request.GET.get('q')

    # what could we do without an alert message
    alert_message = ""

    # build filters
    objects = Idea.objects

    if q:
        words = q.strip().split(" ")
        for word in words:
            objects = objects.filter(Q(name__icontains=word) |
                                     Q(summary__icontains=word) |
                                     Q(detail__icontains=q))
        alert_message += "Icinde " + " ya da ".join(words) + " kelimeleri gecen, "

    if offerred_brand_ids:
        objects = objects.filter(offerred_brands__id__in=offerred_brand_ids)
        brands = Brand.objects.filter(id__in=offerred_brand_ids).all()
        alert_message += " ya da ".join([x.name for x in brands]) + " markalarina sunulmus, "

    if dealt_brand_ids:
        objects = objects.filter(dealt_brands__id__in=dealt_brand_ids)
        brands = Brand.objects.filter(id__in=dealt_brand_ids).all()
        alert_message += " ya da ".join([x.name for x in brands]) + " markalarina satilmis, "

    if category_ids:
        objects = objects.filter(categories__id__in=category_ids)
        categories = Category.objects.filter(id__in=category_ids).all()
        alert_message += " ya da ".join([x.name for x in categories]) + " kategorileri icinde, "

    if budget_ids:
        objects = objects.filter(budget__id__in=budget_ids)
        budgets = Budget.objects.filter(id__in=budget_ids).all()
        alert_message += " ya da ".join([str(x) for x in budgets]) + " butceleri icin, "

    if start_date and end_date:
        start = datetime.strptime(start_date, "%d.%m.%Y")
        end = datetime.strptime(end_date, "%d.%m.%Y")
        objects = objects.filter(date__range=(start, end))
        alert_message += "%s - %s tarihleri arasinda, " % (start_date, end_date)

    ideas = objects.all()

    if ideas.count() == 0:
        alert_message += "hicbir sonuc bulunamadi :("
    else:
        alert_message += "%d sonuc bulundu." % ideas.count()

    messages.add_message(request, messages.INFO,  alert_message)

    # send it to the template
    context = {
        "ideas": ideas, "budget_ids": [int(x) for x in budget_ids],
        "offerred_brand_ids": [int(x) for x in offerred_brand_ids],
        "dealt_brand_ids": [int(x) for x in dealt_brand_ids],
        "category_ids": [int(x) for x in category_ids],
        "start_date": start_date,
        "end_date": end_date,
        "q": q,
    }
    return render_to_response("pool/cms/idea_list.html", context,
                              context_instance=RequestContext(request)
                              )


def undo_last_request(request):
    """undos the latest changes"""
    # First, previous change
    revision = Revision.objects.filter(user=request.user).order_by('-date_created')[1]

    # And revert it, delete=True means we want to delete
    revision.revert(delete=True)

    version_set = revision.version_set.all()
    for version in version_set:
        version.revert()

    # go back to the prev page
    referrer = request.META.get('HTTP_REFERER')
    if referrer:
        return HttpResponseRedirect(referrer)
    else:
        return HttpResponseRedirect("/")


def undo_and_delete_last_request(request):
    """undos the latest changes"""
    # First, get latest revision saved by this user.
    revision = Revision.objects.filter(user=request.user).order_by('-date_created')[0]

    # And revert it, delete=True means we want to delete
    revision.revert(delete=True)

    # delete it dammit
    version_set = revision.version_set.all()
    for version in version_set:
        version.object.delete()

    # go back to the prev page
    referrer = request.META.get('HTTP_REFERER')
    if referrer:
        return HttpResponseRedirect(referrer)
    else:
        return HttpResponseRedirect("/")
