from django.urls import path
from .import views
urlpatterns = [
    path("addbooks/", views.addBooks.as_view(), name="addbooks"),
    path("delbooks/<int:pk>", views.bookdel.as_view(), name="bdelete"),
    path("edit/<int:pk>", views.bookedit.as_view(), name="bedit"),
]
