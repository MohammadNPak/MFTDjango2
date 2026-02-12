from django.contrib import admin
from .models import Post,Comment



class CommentInline(admin.StackedInline):

    model=Comment
    extra = 1
    max_num = 4
    readonly_fields = ["create_at","update_at"]


@admin.decorators.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    readonly_fields=["create_at","update_at"]
    inlines = [CommentInline]

admin.site.register(Comment)
# admin.site.register(Post,PostModelAdmin)
