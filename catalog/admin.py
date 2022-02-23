from django.contrib import admin
from .models import Books, Tags

admin.site.site_header = "Abstract - Панель управления"


admin.site.register(Books)
admin.site.register(Tags)
