from django.conf.urls import url
from . import views
from django.views.generic import ListView, DetailView
from personal.models import NewsPost, CulturePost, ArtPost, MedPost

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^about/', views.about, name = 'about'),
    url(r'^news/$', views.newspost, name = 'news'),
    url(r'^culture/$', views.culturepost, name = 'culture'),
    url(r'^art/$', views.artpost, name = 'art'),
    url(r'^medicine/$', views.medpost, name = 'medicine'),
    url(r'^newsarchive/', ListView.as_view(queryset=NewsPost.objects.all().order_by("-date"),
        template_name="personal/archive.html"), name = 'newsarchive'),
    url(r'^news/(?P<pk>\d+)', DetailView.as_view(model = NewsPost, template_name = 'personal/detailpost.html')),
    url(r'^culturearchive/', ListView.as_view(queryset=CulturePost.objects.all().order_by("-date"),
        template_name="personal/culturearchive.html"), name = 'culturearchive'),
    url(r'^culture/(?P<pk>\d+)', DetailView.as_view(model = CulturePost, template_name = 'personal/detailpost.html')),
    url(r'^artarchive/', ListView.as_view(queryset=ArtPost.objects.all().order_by("-date"),
        template_name="personal/artarchive.html"), name = 'artarchive'),
    url(r'^art/(?P<pk>\d+)', DetailView.as_view(model = ArtPost, template_name = 'personal/detailpost.html')),
    url(r'^medicinearchive/', ListView.as_view(queryset=MedPost.objects.all().order_by("-date"),
        template_name="personal/medicinearchive.html"), name = 'medicinearchive'),
    url(r'^medicine/(?P<pk>\d+)', DetailView.as_view(model = MedPost, template_name = 'personal/detailpost.html'))
    ]
