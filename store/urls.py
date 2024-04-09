
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet
from user.views import CartViewSet
# from products.api import ProductViewSet
router=DefaultRouter()
router.register(r'products',ProductViewSet, basename='products')
router.register(r'cart',CartViewSet, basename='cart')
urlatterns=router.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlatterns)),
    path('user/', include('user.urls')),

]
