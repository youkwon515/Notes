from django.shortcuts import render
from django.urls import reverse
from .models import Memo
from .forms import MemoForm
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
# Create your views here.
class IndexView(ListView):
    model = Memo
    template_name = 'study/index.html'
    context_object_name = 'memos'
    paginate_by = 9
    ordering = ['-dt_created']

class ReviewCreateView(CreateView):
    model = Memo
    form_class = MemoForm
    template_name = 'study/memo_form.html'
    
    def get_success_url(self):
        return reverse("index", kwargs={})

class ReviewUpdateView(UpdateView):
    model = Memo
    form_class = MemoForm
    template_name = 'study/memo_form.html'
    pk_url_kwarg = 'memo_id'

    def get_success_url(self):
        return reverse("index", kwargs={})