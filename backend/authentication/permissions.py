from django.contrib.auth.models import Permission,Group
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from authentication.models import CustomUsers
from products.models import Product

seller_group,created=Group.objects.get_or_create(name='seller')
customer_group,created=Group.objects.get_or_create(name='customer')
content_type=ContentType.objects.get_for_model(Product)
permissions=Permission.objects.filter(content_type=content_type)

for permission in permissions:
    if permission.codename =='view_product':
        customer_group.permissions.add(permission)
        seller_group.permissions.add(permission)
    else:
        seller_group.permissions.add(permission)

user1 = CustomUsers.objects.get(username='chayan')
user1.groups.add(seller_group)
user1.save()

user2=CustomUsers.objects.get(username='Aaru')
user2.groups.add(customer_group)
user2.save()


