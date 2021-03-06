from django.contrib import admin

from .models import Client, Comment, Vechicle



class CommentInline(admin.TabularInline):
    model = Comment


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
admin.site.register(Vechicle)

