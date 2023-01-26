from django.db import models


# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255, help_text='Name of menu item', null=False, unique=True)
    url = models.CharField(default='menu/', max_length=255)
    left = models.IntegerField(blank=True, null=True)
    right = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey(to='self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    level = models.IntegerField(blank=True, null=True)
    root = models.ForeignKey(to='self', blank=True, null=True, related_name='head', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Menu, self).save(*args, **kwargs)
        self.set_mptt()

    def set_mptt(self, left=1, parent=None, level=1, root=None):
        for i in type(self).objects.filter(parent=parent):
            if i.parent is None:
                root = i
            obj, children_count = i, 0
            while obj.children.exists():
                for child in obj.children.all():
                    children_count += 1
                    obj = child
            data = {
                'level': level,
                'left': left,
                'right': left + (children_count * 2) + 1,
                'root': root
            }
            type(self).objects.filter(id=i.id).update(**data)
            left = data['right'] + 1
            self.set_mptt(left=data['left'] + 1, parent=i.id, level=data['level'] + 1, root=root)

    def __str__(self):
        return self.name

    def display_children(self):
        return '\n'.join(child.name for child in self.children.all())

    def display_parent(self):
        return '\n'.join(item.name for item in Menu.objects.all())

    def display_root(self):
        return str(self.root)