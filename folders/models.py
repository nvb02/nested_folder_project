from django.db import models

# Create your models here.


class Folder(models.Model):
    name = models.CharField(max_length=300)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children.all()