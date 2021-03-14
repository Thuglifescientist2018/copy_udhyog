from django.db import models
from django.utils.text import slugify
# Create your models here.


class Sales(models.Model):
    product_name = models.CharField(max_length=255, blank=False, null=True)
    price = models.DecimalField(
        decimal_places=4, max_digits=255, blank=False, null=True)
    quantity = models.CharField(max_length=255, blank=False, null=True)
    slug = models.SlugField(max_length=255, blank=False,
                            null=False, unique=True)
    sold_to = models.CharField(max_length=255, blank=False, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)

        super(Sales, self).save(*args, **kwargs)
