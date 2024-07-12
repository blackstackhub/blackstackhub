from django.contrib import admin
from .models import Fanbase, Product, BlogContent, Blog, Comment

class BlogContentInline(admin.TabularInline):
    model = Blog.contents.through
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(blog__user=request.user)

class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogContentInline]
    exclude = ('contents', 'user',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Fanbase)
admin.site.register(Product)
admin.site.register(BlogContent)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
