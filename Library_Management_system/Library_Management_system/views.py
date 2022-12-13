from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from library.models import Book


class studentview(ListView):
    model = Book
    template_name = "student.html"
    context_object_name = "form"
