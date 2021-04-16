from django.db import models


class App(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=50)
    icon = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    def url(self):
        return '/{}'.format(self.slug)

    def save(self):
        #self.slug = str(self.name).lower().replace(' ', '-') + '-app'
        super().save()
