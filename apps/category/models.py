from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self):
        if self.parent:
            return f'category: {self.title} sub_cate: {self.parent.title}'
        return self.title
