from django.contrib import admin
from forum.models import Forum

# Register your models here.
class ForumAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'addr', 'addr_detail', 'description', 'create_dt', 'modify_dt']

admin.site.register(Forum, ForumAdmin)