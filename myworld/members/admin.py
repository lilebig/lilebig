from django.contrib import admin
from .models import Members, Snippet
# Register your models here.
# admin.site.register([Members, Snippet])
class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)


admin.site.register(Snippet, SnippetAdmin)