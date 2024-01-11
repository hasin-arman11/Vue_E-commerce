from django.db import models
from authentication.models import CustomUsers
# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField()
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category=models.ForeignKey(category, related_name="products",on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    slug=models.SlugField()
    status=models.BooleanField(default=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    description=models.TextField(blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'



class Order(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    ordered_at=models.DateTimeField(auto_now_add=True)
    phone=models.CharField(max_length=12)
    state=models.CharField(max_length=50,null=True,blank=True)
    country=models.CharField(max_length=50,null=True,blank=True)
    post_code=models.CharField(max_length=10,null=True,blank=True)
    users=models.ForeignKey(CustomUsers,on_delete=models.CASCADE,null=True)
    product=models.ManyToManyField(Product,related_name="order_product_items")

    def __str__(self):
        return self.name
    