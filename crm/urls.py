
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import myapp.views as views

urlpatterns = [
	url(r'add_book$', views.add_book, ),
	url(r'show_books$', views.show_books, ),
	url(r'^$', TemplateView.as_view(template_name="index.html")),
]

