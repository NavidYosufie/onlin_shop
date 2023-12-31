from django.contrib import admin
from . import models


class InformationAdmin(admin.StackedInline):
    model = models.Information


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", 'slug',"parent")
    prepopulated_fields = {'slug': ('title', )}



class CommentInline(admin.StackedInline):
    model = models.Comment
    extra = 0


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", 'status',)
    list_filter = ('status', 'created_at')
    search_fields = ('title',)
    inlines = (InformationAdmin, CommentInline,)


admin.site.register(models.Size)
admin.site.register(models.Color)
