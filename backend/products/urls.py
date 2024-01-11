from django.urls import path,include
from .views import (ProductView,
                    OrderAPIView,
                    ProductDetails,
                    Categoryview,
                    AllCategoryView,
                    Searchview,
                    ProductUpadateView,
                    ProductGenericView,
                    createProductView,
                    productListCreateView,
                    ProductRetrieveUpdateDestroyView
                    )

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'items', Searchview)
urlpatterns = [
    path('', include(router.urls)),
    path('products/',ProductView.as_view(),name="products"),
    path('update/<int:pk>/',ProductUpadateView.as_view(),name="update"),
    path('<slug:category_slug>/<slug:product_slug>/',ProductDetails.as_view(),name="product"),
    path('orders/',OrderAPIView.as_view(),name="orders_api"),
    path('categories/',AllCategoryView.as_view(),name="categories"),
    # path('<slug:category_slug>/',Categoryview.as_view(),name="category"),

    # Generic api views
    # path('get_product/<int:pk>/',ProductRetrieveUpdateDestroyView.as_view(),name="retrives"),
    # path('list_create_products/',productListCreateView.as_view(),name="list_create"),
    # path('generic_products/',createProductView.as_view(),name="create"),
    # path('all_products/',ProductGenericView.as_view(),name="products"),  
]
