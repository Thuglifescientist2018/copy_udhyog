from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.utils.text import slugify
# Create your models here.


class PurchasesQuerySet(models.QuerySet):
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


class PurchasesManager(models.Manager):
    def get_queryset(self):
        return PurchasesQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class Purchases(models.Model):
    product_name = models.CharField(max_length=255, blank=False, null=True)
    price = models.DecimalField(
        decimal_places=4, max_digits=255, blank=False, null=True)
    quantity = models.CharField(max_length=255, blank=False, null=True)
    slug = models.SlugField(max_length=255, blank=False,
                            null=False, unique=True)
    bought_from = models.CharField(max_length=255, blank=False, null=True)
    pending_amount = models.DecimalField(
        decimal_places=4, max_digits=255, blank=True, null=True)

    date = models.DateField(auto_now=False, blank=True, null=True)
    objects = PurchasesManager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Purchases, self).save(*args, **kwargs)

    def actual_price(self, *args, **kwargs):
        actual_price = float(self.price) * float(self.quantity)
        return actual_price

    def total_price():
        price = 0
        purchases = Purchases.objects.all()
        for purchase in purchases:
            price += float(purchase.actual_price())
        total_amount = TotalAmount()
        total_amount.total_amount = price
        total_amount.save()
        return price


class TotalAmount(models.Model):
    model = models.ForeignKey(
        Purchases, on_delete=models.SET_NULL, null=True)
    total_amount = models.DecimalField(
        blank=True, null=True, decimal_places=4, max_digits=255)
