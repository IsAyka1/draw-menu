from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255, help_text='Name of menu item', null=False, unique=True)
    url = models.CharField(default='menu/', max_length=255)
    is_root = models.BooleanField(default=True)
    children = models.ManyToManyField('self', null=True, symmetrical=False, blank=True)

    def __str__(self):
        return self.name

    def display_children(self):
        return '\n'.join(child.name for child in self.children.all())

