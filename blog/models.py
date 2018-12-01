from django.db import models
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
import tagulous.models


class Post(models.Model):
    title = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=16,
                              choices=(
                                  ('draft', 'Draft'),
                                  ('published', 'Published'),
                              ))
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail_image = models.ImageField(upload_to='blog/thumbnails/%Y/%m/%d')
    description = models.TextField()
    contents = MarkdownxField()
    post_tag = tagulous.models.TagField(force_lowercase=True)

    @property
    def formatted_markdown(self):
        return markdownify(self.contents)

    def __str__(self):
        return self.title