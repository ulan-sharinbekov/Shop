from django.db import models

# Create your models here.

class Catalog(models.Model):
    GROUP_CHOICES = [
        ('ODEZHDA', 'odezhda'),
        ('OBUV', 'Obuv'),
        ('BRUKI', 'Bruki'),
        ('SHAPKI', 'Shapki'),

    ]
    parent = models.ForeignKey('self',  on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=False)
    group = models.CharField(max_length=100, choices=GROUP_CHOICES, default='ODEZHDA')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class SIZE_Prod(models.Model):
    SIZE_CHOICES = [
        ('75_85', 'XS'),
        ('100_120', 'XSS'),
        ('130_140', 'SXS'),
        ('XS', 'XS'),
        ('XS', 'XS'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
    ]

    name = models.CharField(max_length=100, choices=SIZE_CHOICES, default='S')

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "Размеры"

    def __str__(self):
        return self.name



class Product(models.Model):

    catalog = models.ForeignKey(Catalog,  on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255,  null=True)
    article = models.CharField(max_length=12, null=False, unique=True)
    image = models.ImageField(upload_to='api/image/', height_field=None, width_field=None, max_length=100, default='api/image/def.jpg')
    size = models.ForeignKey(SIZE_Prod, on_delete=models.CASCADE, null=False)
    price = models.FloatField()
    quantity = models.FloatField()
    amount = models.FloatField()



    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def get_sum(self):
        self.amount = self.price * self.quantity

    def __str__(self):
        return self.name