from django.db import models
from django.utils.html import format_html
import django.utils.timezone
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit
from ckeditor.fields import RichTextField
from django.utils.html import strip_tags


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    intro = RichTextField()
    body = RichTextField()
    publish = models.BooleanField()
    created_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField()

    def intro_strip(self):
        return strip_tags(self.intro)


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = ProcessedImageField(verbose_name='Image here',
                                processors=[ResizeToFit(1000, 1000)],
                                upload_to='upload_folder')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(144, 144)],
                                     format='JPEG',
                                     options={'quality': 80})
    pub_date = models.DateTimeField(default=django.utils.timezone.now)

    def image_disp(self):
        return format_html('<img src="{}" />', self.image_thumbnail.url)
