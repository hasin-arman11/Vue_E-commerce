from rest_framework import serializers
from .models import Product,category,Order

class product_serializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','slug','product_name','price','description','category','get_absolute_url']

class category_serializer(serializers.ModelSerializer):
    products=product_serializer(many=True)
    class Meta:
        model=category
        fields=['id','name','products','slug']

class order_serializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=[
            "name",
            "email",
            "address",
            "country",
            "post_code",  
            "phone",
            'users',
            'product'
        ]
    

        