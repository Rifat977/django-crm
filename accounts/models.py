from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    CATEGORY = (
    ('Indoor', 'Indoor'),
    ('Outdoor', 'Outdoor')
    )
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    categorty = models.CharField(max_length=200,choices=CATEGORY)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, related_name="customer_order")
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name="product_order")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return f"{self.product} ${self.product.price}"
