from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu', kwargs={'menu_name': self.slug})

    class Meta:
        ordering = [id]


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, null=True, blank=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    url_is_named = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    menu = models.ForeignKey('menu', on_delete=models.CASCADE, related_name='item', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.url_is_named:
            return reverse('menu_item', kwargs={'menu_name': self.menu.slug, 'item_name': self.slug})
        else:
            return self.url

    class Meta:
        ordering = ['id']
