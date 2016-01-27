from django.contrib import admin

# Register your models here.

from .models import Mysite,ProductInfo

class ShowMysite(admin.ModelAdmin):
    list_display = ('title', 'url', 'author', 'num')
    search_fields = ('title', 'author')

class ShowProductInfo(admin.ModelAdmin):
    list_display = ('symbol', 'cn_name', 'issue_type')
    search_fields = ('symbol', 'cn_name')

admin.site.register(Mysite, ShowMysite)
admin.site.register(ProductInfo, ShowProductInfo)
