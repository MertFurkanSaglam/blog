from django.contrib import admin
from .models import Blog, Category


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","slug") #admin panelinde nelerin gözükmesini istiyorsun
    list_editable = ("is_active","is_home") #hangilerini ayarlamak istiyorsun(text olanları değiştirmeyi denedim yapamadım)
    search_fields = ("title","description") #arama butonu nerede arama yapacağını seçiyorsun
    readonly_fields = ("slug",) #edit yapılmasını engelleyip sadece okunmasına olanak sağlıyor
    list_filter = ("category","is_active","is_home") #sağ tarafta çıkan kısa filtreleme yolu




admin.site.register(Blog,BlogAdmin)#solüstteki panelde ayrı bir alan açar ve oradan diğer alanlara erişim sağlayabilirsin
admin.site.register(Category)