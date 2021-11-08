from django.contrib import admin
from .models import Post, PostImages, Comments


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "text", "url")
    list_display_links = ("title", )



admin.site.register(PostImages)
admin.site.register(Post, CategoryAdmin)
admin.site.register(Comments)

