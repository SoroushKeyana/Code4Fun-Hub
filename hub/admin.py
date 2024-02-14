# admin.py
from django.contrib import admin
from .models import Project, ForumPost, ForumCategory
from .forms import ProjectForm

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm

admin.site.register(Project, ProjectAdmin)
admin.site.register(ForumPost)

@admin.register(ForumCategory)
class ForumCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
