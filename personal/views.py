from django.shortcuts import render
from personal.models import About, NewsPost, CulturePost, ArtPost, MedPost
from django.views import generic

def index(request):
    return render(request, 'personal/home.html')

def about(request):
    abinfo = About.objects.all()
    return render(request, 'personal/about.html', {'content': abinfo})

def newspost(request):
    latest_blog_post = [NewsPost.objects.latest('date')]  #think have to add filter then [1] to return newest...
    return render(request, 'personal/newspostpage.html', {'post': latest_blog_post})

#write same style view for Culture, Art, med,

def culturepost(request):
    latest_culture_post = [CulturePost.objects.latest('date')]
    return render(request, 'personal/culturepostpage.html', {'post': latest_culture_post})

def artpost(request):
    latest_art_post = [ArtPost.objects.latest('date')]
    return render(request, 'personal/artpostpage.html', {'post': latest_art_post})

def medpost(request):
    latest_med_post = [MedPost.objects.latest('date')]
    return render(request, 'personal/medpostpage.html', {'post': latest_med_post})
