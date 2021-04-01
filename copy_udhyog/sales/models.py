from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.utils.text import slugify
# Create your models here.


class SalesQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        # lte = lesser than oe equal to
        return self.filter(date__gte=now)

    def search(self, query):
        lookup = (Q(product_name__icontains=query)
                  | Q(slug__icontains=query)
                  | Q(date__icontains=query)

                  # or whatever

                  )
        return self.filter(lookup)


class SalesManager(models.Manager):
    def get_queryset(self):
        return SalesQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class Sales(models.Model):
    product_name = models.CharField(max_length=255, blank=False, null=True)
    price = models.DecimalField(
        decimal_places=4, max_digits=255, blank=False, null=True)
    quantity = models.CharField(max_length=255, blank=False, null=True)
    slug = models.SlugField(max_length=255, blank=False,
                            null=False, unique=True)
    sold_to = models.CharField(max_length=255, blank=False, null=True)
    date = models.DateField(auto_now=False, blank=True, null=True)
    objects = SalesManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)

        super(Sales, self).save(*args, **kwargs)

    def actual_price(self, *args, **kwargs):
        actual_price = float(self.price) * float(self.quantity)
        return actual_price
