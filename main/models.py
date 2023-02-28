from django.db import models
from django.utils import timezone
import uuid
from django.core.exceptions import ValidationError

def min_value_validator(value):
    if value < 0:
        raise ValidationError(
            '%(value)s must be greater than or equal to 0',
            params={'value': value},
        )
def generate_product_id():
    product_id = str(uuid.uuid4())[:16].replace('-', '').lower()
    return product_id

class BaseModel(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Base Model'


class Category(BaseModel):
    stock_in = '1'
    stock_out = '0'
    STATUS = (
        (stock_out, 'STOCK_OUT'),
        (stock_in, 'STOCK_IN')
    )

    name = models.CharField(
        max_length=255,
        verbose_name='Category name'
    )
    description = models.TextField(
        verbose_name='category description'
    )
    status = models.CharField(
        max_length=255,
        verbose_name='Status',
        choices=STATUS,
        default=STATUS[0][0]
    )

    class Meta:
        verbose_name = 'Category'

    def __str__(self):
        return self.name

class Product(BaseModel):
    inactive = '0'
    active = '1'

    STATUSES = (
        (inactive, 'InActive'),
        (active, 'Active')
    )

    name = models.CharField(
        max_length=255,
        verbose_name='Product name'
    )
    product_id = models.CharField(
        max_length=255,
        verbose_name='Product id',
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        on_delete=models.CASCADE,
        to=Category,
        related_name='Category'
    )
    description = models.TextField(
        verbose_name='Product description'
    )
    price = models.DecimalField(
        verbose_name='Product price',
        max_digits=10,
        decimal_places=2,
        validators=[min_value_validator]
    )
    status = models.CharField(
        max_length=255,
        verbose_name='Product Status',
        choices=STATUSES,
        default=STATUSES[0][0]
    )

    class Meta:
        verbose_name = 'Product'

    def save(self, *args, **kwargs):
        self.product_id = generate_product_id()
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
