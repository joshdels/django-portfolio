from django.contrib import admin
from .models import Project, ProjectBlock, ProjectTag


class ProjectBlockInline(admin.TabularInline):
    model = ProjectBlock
    extra = 1
    ordering = ("order",)
    fields = ("block_type", "text", "image", "order")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "display_tags", "created_at")
    inlines = [ProjectBlockInline]

    filter_horizontal = ("tags",)

    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    display_tags.short_description = "Tags"


@admin.register(ProjectTag)
class ProjectTagAdmin(admin.ModelAdmin):
    list_display = ("name",)
