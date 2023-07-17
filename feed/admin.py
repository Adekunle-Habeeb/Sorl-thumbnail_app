from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    pass

    def __str__(self):
        return self.text


admin.site.register(Post, PostAdmin)
