#from django.shortcuts import render
from django.views.generic import ListView
from models import (
    Idea
)


class IdeaList(ListView):
    model = Idea
    context_object_name = "ideas"
    paginate_by = 2


class IdeaDetail(DetailView):
    model = Idea
