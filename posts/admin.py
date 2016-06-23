from django.contrib import admin

from posts.models import Post, Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_disp', 'pub_date')
    list_per_page = 10

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'intro_strip', 'publish')


admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
