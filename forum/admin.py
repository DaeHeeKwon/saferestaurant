from django.contrib import admin
from forum.models import Forum

# Register your models here.
class ForumAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'addr']

admin.site.register(Forum, ForumAdmin)