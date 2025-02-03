from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import product_serializer, category_serializer, order_serializer
# from authentication.models import CustomUsers
from .models import Product, category, Order
from django.http import Http404, HttpResponse
from rest_framework import generics,mixins
from authentication import permissions


class ProductView(APIView):
    permission_classes=[AllowAny]
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(status=True)
        serializer = product_serializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        payload = request.data.copy()
        payload['slug'] = payload['product_name'][0].lower()
        payload['file'] = request.FILES.get('file')
        print('payload------>',request.FILES.get('file'))
        serializer = product_serializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductUpadateView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = product_serializer(snippet)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        payload = request.data
        payload['slug'] = payload['product_name'].lower()
        serializer = product_serializer(snippet, data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductDetails(APIView):
    permission_classes=[AllowAny]
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug, slug=product_slug)
        except Product.DoesNotExist:
            return Http404

    def get(self, request, *args, **kwargs):
        category_slug = kwargs['category_slug']
        product_slug = kwargs['product_slug']

        single_product = self.get_object(category_slug, product_slug)
        serializer = product_serializer(single_product, many=True)
        return Response(serializer.data)
    
  

class AllCategoryView(APIView):
    permission_classes=[AllowAny]
    def get(self, request, *args, **kwargs):
        categories = category.objects.all()
        serializer = category_serializer(categories, many=True)
        return Response(serializer.data)


class Categoryview(APIView):
    permission_classes=[AllowAny]
    def get(self, request,*args, **kwargs):
        category_item = kwargs['category_slug']
        product=Product.objects.filter(category__slug=category_item)
        serializer = product_serializer(product,many=True)
        return Response(serializer.data)


class Searchview(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    queryset = Product.objects.all()
    serializer_class = product_serializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('product_name', 'description')


class OrderAPIView(APIView):
    def post(self, request, *args, **kwargs):
        products=[]
        for i in range(0,len(request.data["items"])):
           products.append(request.data["items"][i]['product']['id'])
        product_list=Product.objects.filter(id__in=products)

        ordered=Order.objects.create(
            name=request.data['name'],
            address=request.data['address'],
            email=request.data['email'],
            phone=request.data['phone'],
            state=request.data['state'],
            country=request.data['country'],
            post_code=request.data['post_code'], 
            users = request.user
        )
        ordered.product.set(product_list)
        ordered.save()
        return Response(data={'success':'item saved successfully'})
    
    def get(self,request,*args, **kwargs):
        Ordered_items=Order.objects.all()
        serializer=order_serializer(Ordered_items,many=True)
        return Response(serializer.data)
    

# Generic Api Views
class ProductGenericView(mixins.ListModelMixin, mixins.CreateModelMixin,mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = product_serializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        request.data['slug']=request.data['product_name'].lower()
        return self.create(request,*args, **kwargs)
    
    
class createProductView(mixins.ListModelMixin,generics.CreateAPIView):
    serializer_class=product_serializer
    queryset=Product.objects.all()

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
class productListCreateView(generics.ListCreateAPIView):
    serializer_class= product_serializer
    queryset = Product.objects.all()

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class= product_serializer



