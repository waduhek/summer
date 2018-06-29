from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 255, unique = True)

    slug = models.SlugField(max_length = 255, unique = True)

    image = models.ImageField(default = None, blank = True)

    description = models.TextField(blank = True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return 'Category {}'.format(self.name)

class Product(models.Model):
    manufacturer = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    slug = models.SlugField(max_length = 255, unique = True)

    image = models.ImageField(default = None)

    description = models.TextField()

    price = models.DecimalField(max_digits = 12, decimal_places = 2)

    stock = models.PositiveIntegerField()
    available = models.BooleanField(default = True)

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('name', 'created', 'updated', )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return '{}: {} {}'.format(self.category, self.manufacturer, self.name)