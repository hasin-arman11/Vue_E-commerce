
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('admin/', admin.site.urls),
    path('',include('products.urls')),
    path('',include('authentication.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
