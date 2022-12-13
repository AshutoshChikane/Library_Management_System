from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Book
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.


@method_decorator(login_required(login_url='/sign_in/'), name="dispatch")
class addBooks(CreateView):
    model = Book
    fields = "__all__"
    template_name = "addbook.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lis"] = Book.objects.all()
        return context

    def get_success_url(self):
        return reverse("addbooks")


@method_decorator(login_required(login_url='/sign_in_out/signin/'), name="dispatch")
class bookdel(DeleteView):
    model = Book
    template_name = 'bookdelete.html'

    def get_success_url(self):
        return reverse("addbooks")


@method_decorator(login_required(login_url='/sign_in_out/signin/'), name="dispatch")
class bookedit(UpdateView):
    model = Book
    fields = "__all__"
    template_name = "bookedit.html"
    context_object_name = "form"

    def get_success_url(self):
        return reverse("addbooks")
