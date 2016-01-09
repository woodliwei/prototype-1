from django.contrib import admin

# Register your models here.

from prototype.models import Mysite

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'author', 'num')
    search_fields = ('title', 'author')

admin.site.register(Mysite)
