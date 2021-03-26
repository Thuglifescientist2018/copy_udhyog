from django.db import models

from django.utils.text import slugify
# Create your models here.


class Purchases(models.Model):
    product_name = models.CharField(max_length=255, blank=False, null=True)
    price = models.DecimalField(
        decimal_places=4, max_digits=255, blank=False, null=True)
    quantity = models.CharField(max_length=255, blank=False, null=True)
    slug = models.SlugField(max_length=255, blank=False,
                            null=False, unique=True)
    bought_from = models.CharField(max_length=255, blank=False, null=True)
    date = models.DateField(auto_now=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Purchases, self).save(*args, **kwargs)

    def actual_price(self, *args, **kwargs):
        actual_price = float(self.price) * float(self.quantity)
        return actual_price
