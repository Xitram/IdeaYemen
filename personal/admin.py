from django.contrib import admin
from personal.models import About, NewsPost, CulturePost, MedPost, ArtPost

admin.site.register(About)
admin.site.register(NewsPost)
admin.site.register(CulturePost)
admin.site.register(MedPost)
admin.site.register(ArtPost)
