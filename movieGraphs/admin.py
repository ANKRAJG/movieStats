from django.contrib import admin
from . import models
from .models import Hollywood, Profession, Artist, Xaxis, Yaxis, MovieImage, ArtistImage


class ArtistInline(admin.StackedInline):
    model = Artist
    extra = 4
    
class ProfessionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['prof_name']}),
    ]
    inlines = [ArtistInline]
    

admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Hollywood)
admin.site.register(Xaxis)
admin.site.register(Yaxis)
admin.site.register(MovieImage)
admin.site.register(ArtistImage)
